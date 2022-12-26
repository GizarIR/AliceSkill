import enum
import inspect
import sys
from abc import ABC, abstractmethod
from typing import Optional
import json

import intents
from request import Request
from response_helpers import (
    button,
    image_gallery,
)
from state import STATE_REQUEST_KEY, STATE_RESPONSE_KEY


class Prof(enum.Enum):
    UNKNOWN = 1
    ANALYST = 2
    TESTER = 3

    @classmethod
    def from_request(cls, request: Request, intent_name: str):
        # slots = request.intents
        slot = request.intents.get(intent_name, {})
        # print(f'СЛОТЫ Тип: {type(slots)}, Значение: {slots}, Один слот: {slot} ')
        if slot != {}:
            slot = request.intents[intent_name]['slots']['prof']['value']
        if slot == 'analyst':
            return cls.ANALYST
        elif slot == 'tester':
            return cls.TESTER
        else:
            return cls.UNKNOWN


def move_to_prof_scene(request: Request, intent_name: str):
    prof = Prof.from_request(request, intent_name)
    if prof == Prof.ANALYST:
        return Analyst()
    elif prof == Prof.TESTER:
        return Tester()
    else:
        return UnknownProf()


class Scene(ABC):

    @classmethod
    def id(cls):
        return cls.__name__

    """Генерация ответа сцены"""
    @abstractmethod
    def reply(self, request):
        raise NotImplementedError()

    """Проверка перехода к новой сцене"""
    def move(self, request: Request):
        next_scene = self.handle_local_intents(request)
        if next_scene is None:
            next_scene = self.handle_global_intents(request)
        return next_scene

    @abstractmethod
    def handle_global_intents(self):
        raise NotImplementedError()

    @abstractmethod
    def handle_local_intents(request: Request) -> Optional[str]:
        raise NotImplementedError()

    def fallback(self, request: Request):
        return self.make_response('Извините, я вас не поняла. Пожалуйста, попробуйте переформулировать.')

    def make_response(self, text, tts=None, card=None, state=None, buttons=None, directives=None):
        response = {
            'text': text,
            'tts': tts if tts is not None else text,
        }
        if card is not None:
            response['card'] = card
        if buttons is not None:
            response['buttons'] = buttons
        if directives is not None:
            response['directives'] = directives
        webhook_response = {
            'response': response,
            'version': '1.0',
            STATE_RESPONSE_KEY: {
                'scene': self.id(),
            },
        }
        if state is not None:
            webhook_response[STATE_RESPONSE_KEY].update(state)
        return webhook_response


class TestTourScene(Scene):

    def handle_global_intents(self, request):
        if intents.START_TOUR_TEST in request.intents:
            return WelcomeTest()


class WelcomeTest(TestTourScene):
    def reply(self, request: Request):
        # scenes = str(SCENES)
        text = ('Добро пожаловать, давайте пройдем тест. '
                'Начнем?')
        return self.make_response(
            text,
            buttons=[
                button('Да', hide=True),
                button('Нет', hide=True),
            ],
        )

    def handle_local_intents(self, request: Request):
        if intents.U_YES in request.intents:
            return Query_1()
        # по умолчанию если не условие то уйдет в fallback


class Query_1(TestTourScene):
    def reply(self, request: Request):
        text = ('Поздравляем вы прошли тест. Хотите поговорить о профессиях?')
        return self.make_response(
            text,
            buttons=[
                button('Да', hide=True),
                button('Нет', hide=True),
            ],
        )

    def handle_local_intents(self, request: Request):
        if intents.U_YES in request.intents:
            return StartTour()



class StartTour(TestTourScene):
    def reply(self, request: Request):
        text = 'Отлично! Давайте поговорим о профессиях? О какой бы Вы хотели?'
        return self.make_response(
            text,
            state={
                'screen': 'start_tour'
            },
            buttons=[
                button('Аналитик'),
                button('Тестировщик'),
            ]
        )

    def handle_local_intents(self, request: Request):
        if intents.START_TOUR_WITH_PROF_SHORT:
            return move_to_prof_scene(request, intents.START_TOUR_WITH_PROF_SHORT)


class Analyst(TestTourScene):
    def reply(self, request: Request):
        return self.make_response(
            text='В будущем здесь появится рассказ об Аналитике. О ком еще рассказать?',
            state={
                'screen': 'start_tour'
            },
            buttons=[
                button('Аналитик'),
                button('Тестировщик'),
            ]
        )

    def handle_local_intents(self, request: Request):
        if intents.START_TOUR_WITH_PROF_SHORT:
            return move_to_prof_scene(request, intents.START_TOUR_WITH_PROF_SHORT)


class Tester(TestTourScene):
    def reply(self, request: Request):
        return self.make_response(
            text='В будущем здесь появится рассказ об Тестеровщике. О ком еще рассказать?',
            state={
                'screen': 'start_tour'
            },
            buttons=[
                button('Аналитик'),
                button('Тестировщик'),
            ]
        )

    def handle_local_intents(self, request: Request):
        if intents.START_TOUR_WITH_PROF_SHORT:
            return move_to_prof_scene(request, intents.START_TOUR_WITH_PROF_SHORT)


class UnknownProf(TestTourScene):
    def reply(self, request: Request):
        return self.make_response(
            text='Я такой профессии не знаю. О ком еще рассказать?',
            state={
                'screen': 'start_tour'
            },
            buttons=[
                button('Аналитик'),
                button('Тестировщик'),
            ]
        )

    def handle_local_intents(self, request: Request):
        if intents.START_TOUR_WITH_PROF_SHORT:
            return move_to_prof_scene(request, intents.START_TOUR_WITH_PROF_SHORT)



def _list_scenes():
    current_module = sys.modules[__name__]
    scenes = []
    for name, obj in inspect.getmembers(current_module):
        if inspect.isclass(obj) and issubclass(obj, Scene):
            scenes.append(obj)
    return scenes


SCENES = {
    scene.id(): scene for scene in _list_scenes()
}

DEFAULT_SCENE = WelcomeTest
