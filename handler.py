# Для работы функционала сохранения state сессии, необходимо
# включить настройку навыка "Использовать хранилище данных в навыке"

import json

from state import STATE_REQUEST_KEY, STATE_RESPONSE_KEY
from scenes import SCENES, DEFAULT_SCENE
from request import Request


def handler(event, context):
    print('Входящий запрос: ' + json.dumps(event))
    request = Request(event)
    current_scene_id = event.get('state', {}).get(STATE_REQUEST_KEY, {}).get('scene')
    print('Текущая сцена: ' + str(current_scene_id))
    if current_scene_id is None:
        return DEFAULT_SCENE().reply(request)
    current_scene = SCENES.get(current_scene_id, DEFAULT_SCENE)()
    next_scene = current_scene.move(request)
    if next_scene is not None:
        print(f'Переход из сцены {current_scene.id()} в {next_scene.id()}')
        return next_scene.reply(request)
    else:
        print(f'Ошибка в разборе пользовательского запроса в сцене {current_scene.id()}')
        return current_scene.fallback(request)
