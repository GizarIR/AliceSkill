# Самый простой обработчик для Навыка Алисы
# Для работы необходимо зарегистрировать новый интент 'hello'

STATE_REQUEST_KEY = 'session'
STATE_RESPONSE_KEY = 'session_state'


def make_response(text):
    print(f'Print anything to log! ')
    return {
        'response': {
            'text': text,
        },
        'version': '1.0',
    }

def fallback(event):
    return make_response('Извините, я Вас не поняла. Пожалуйста, попробуйте переформулировать.')

def handler(event, context):
    intents = event['request'].get('nlu', {}).get('intents')

    if event['session']['new']:
        return make_response(text='Привет Мир... емае')
    elif 'hello' in intents:
        return make_response(text='Привет привет тебе дорогой ты мой человек')
    else:
        return fallback(event)
