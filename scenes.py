import enum
import inspect
import sys
from abc import ABC, abstractmethod
from typing import Optional

import intents
from request import Request
from response_helper import (
    button,
    image_gallery,
)
from state import STATE_RESPONSE_KEY

class Prof(enum.Enum):
    UNKNOWN = 1
    ANALYST = 2
    TESTER = 3
    DEVLOPER = 4

    @classmethod
    def from_request(cls, request: Request, intent_name: str):
        slot = request.intents[intent_name]['slots']['prof']['value']
        if slot == 'analyst':
            return cls.ANALYST
        elif slot == 'tester':
            return cls.TESTER
        elif slot == 'developer':
            return cls.DEVELOPER
        else:
            return cls.UNKNOWN


def move_to_prof_scene(request: Request, intent_name: str):
    prof = Prof.from_request(request, intent_name)
    if prof == Prof.ANALYST:
        return Analyst()
    elif prof == Prof.CATHEDRAL:
        return Tester()
    elif prof == Prof.DEVELOPER:
        return Developer()
    else:
        return UnknownPlace()


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


class ProfTourScene(Scene):

    def handle_global_intents(self, request):
        if intents.START_TOUR in request.intents:
            return StartTour()
        elif intents.START_TOUR_WITH_PROF in request.intents:
            return move_to_prof_scene(request, intents.START_TOUR_WITH_PROF)

class Welcome(ProfTourScene):
    def reply(self, request: Request):
        text = ('Добро пожаловать, тут я рассказываю о самых интересных и востребованных АйТи профессиях. '
                'Начнем?')
        return self.make_response(
            text,
            state={
                'scene': 'welcome'
            },
            buttons=[
                button('Да', hide=True),
                button('Нет', hide=True),
            ],
        )

    def handle_local_intents(self, request: Request):
        if intents.U_YES:
            return move_to_prof_scene(request, intents.START_TOUR)

class StartTour(ProfTourScene):
    def reply(self, request: Request):
        text = 'Я знаю огромное количество профейссий в ИТ, для начала могу рассказать об Аналитике?'
        return self.make_response(
            text,
            state={
                'screen': 'start_tour'
            },
            buttons=[
                button('Аналитик'),
                button('Тестировщик'),
                button('Разработчик'),
            ]
        )

    def handle_local_intents(self, request: Request):
        if intents.U_YES:
            return move_to_prof_scene(request, intents.START_TOUR_WITH_PLACE_SHORT)


class Analyst(ProfTourScene):
    def reply(self, request: Request):
        tts = ('В будущем здесь появится описание Аналитика')
        return self.make_response(
            text,
            buttons=[
                button('Аналитик'),
                button('Тестировщик'),
                button('Разработчик'),
            ]
        )

    def handle_local_intents(self, request: Request):
        pass


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

DEFAULT_SCENE = Welcome

