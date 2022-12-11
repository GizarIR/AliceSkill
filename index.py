STATE_REQUEST_KEY = 'session'
STATE_RESPONSE_KEY = 'session_state'


def make_response(text, tts=None, card=None, state=None, buttons=None):
    response = {
        'text': text,
        'tts': tts if tts is not None else text,
    }
    if card is not None:
        response['card'] = card
    webhook_response = {
        'response': response,
        'version': '1.0',
    }
    if state is not None:
        webhook_response[STATE_RESPONSE_KEY] = state
    if buttons:
        response['buttons'] = buttons
    return webhook_response


def button(title, payload=None, url=None, hide=False):
    button = {
        'title': title,
        'hide': hide,
    }
    if payload is not None:
        button['payload'] = payload
    if url is not None:
        button['url'] = url
    return button


def image_gallery(image_ids):
    items = [{'image_id': image_id} for image_id in image_ids]
    return {
        'type': 'ImageGallery',
        'items': items,
    }


def welcome_message(event):
    text = ('Добро пожаловать, тут я могу помочь вам найти для себя новую профессию. '
            'Расскажу о самых интересных и востребованных IT профессий. '
            'Вы знаете какое направление вас интересует?')
    return make_response(text, buttons=[
        button('Расскажи про профессии', hide=True),
    ])

def start_tour(event):
    text = ('Сфера АйТи очень огромна, в ней есть множество различных профессий. '
            'О какой специальности рассказать подробнее?')
    return make_response(text, state={
        'screen': 'start_tour',
    }, buttons=[
        button('Аналитик'),
        button('Тестировщик'),
    ])

def get_analyst(event):
    tts = ('Аналитик sil<[1000]> Аналитик - это специалист, который занимается выявлением'
            'бизнес-проблем, выяснению потребностей заинтересованных сторон,' 
            'обоснованию решений и обеспечению проведения изменений в организации.'
    )
    return make_response(
        text='',
        tts=tts,STATE_REQUEST_KEY = 'session'
STATE_RESPONSE_KEY = 'session_state'


def make_response(text, tts=None, card=None, state=None, buttons=None):
    response = {
        'text': text,
        'tts': tts if tts is not None else text,
    }
    if card is not None:
        response['card'] = card
    webhook_response = {
        'response': response,
        'version': '1.0',
    }
    if state is not None:
        webhook_response[STATE_RESPONSE_KEY] = state
    if buttons:
        response['buttons'] = buttons
    return webhook_response


def button(title, payload=None, url=None, hide=False):
    button = {
        'title': title,
        'hide': hide,
    }
    if payload is not None:
        button['payload'] = payload
    if url is not None:
        button['url'] = url
    return button


def image_gallery(image_ids):
    items = [{'image_id': image_id} for image_id in image_ids]
    return {
        'type': 'ImageGallery',
        'items': items,
    }


def welcome_message(event):
    text = ('Добро пожаловать, тут я могу помочь вам найти для себя новую профессию. '
            'Расскажу о самых интересных и востребованных IT профессий. '
            'Вы знаете какое направление вас интересует?')
    return make_response(text, buttons=[
        button('Расскажи про профессии', hide=True),
    ])

def start_tour(event):
    text = ('Сфера АйТи очень огромна, в ней есть множество различных профессий. '
            'О какой специальности рассказать подробнее?')
    return make_response(text, state={
        'screen': 'start_tour',
    }, buttons=[
        button('Аналитик'),
        button('Тестировщик'),
    ])

def get_analyst(event):
    tts = ('Аналитик sil<[1000]> Аналитик - это специалист, который занимается выявлением'
            'бизнес-проблем, выяснению потребностей заинтересованных сторон,' 
            'обоснованию решений и обеспечению проведения изменений в организации.'
    )
    return make_response(
        text='',
        tts=tts,
        card=image_gallery(image_ids=[
            '965417/c21764e6199631467555',
            '1540737/e958a13e0e9801227c06',
        ])
    )


def start_tour_with_prof(event, intent_name='start_tour_with_prof'):
    intent = event['request']['nlu']['intents'][intent_name]
    prof = intent['slots']['prof']['value']
    if prof == 'analyst':
        return get_analyst(event)
    elif prof == 'tester':
        return make_response(text='Здесь появиться текст про Тестировщика')
    elif prof == 'developer':
        return make_response(text='Здесь появиться текст про Разработчика')
    elif prof == 'project_manager':
        return make_response(text='Здесь появиться текст про Проджект менеджера')
    elif prof == 'designer':
        return make_response(text='Здесь появиться текст про Дизайнера')
    else:
        return fallback(event)

def fallback(event):
    return make_response(
        'Извините, я Вас не поняла. Пожалуйста, попробуйте переформулировать.',
        state=event['state'][STATE_REQUEST_KEY])


def handler(event, context):
    intents = event['request'].get('nlu', {}).get('intents')
    state = event.get('state').get(STATE_REQUEST_KEY, {})
    if event['session']['new']:
        return welcome_message(event)
    elif 'start_tour' in intents:
        return start_tour(event)
    elif 'start_tour_with_prof' in intents:
        return start_tour_with_prof(event)
    elif state.get('screen') == 'start_tour' and 'start_tour_with_prof_short' in intents:
        # здесь может быть любой другой обработчик в соответсвии с интентом и статусом
        return start_tour_with_prof(event, intent_name='start_tour_with_prof_short')
    else:
        return fallback(event)

        card=image_gallery(image_ids=[
            '965417/c21764e6199631467555',
            '1540737/e958a13e0e9801227c06',
        ])
    )


def start_tour_with_prof(event, intent_name='start_tour_with_prof'):
    intent = event['request']['nlu']['intents'][intent_name]
    prof = intent['slots']['prof']['value']
    if prof == 'analyst':
        return get_analyst(event)
    elif prof == 'tester':
        return make_response(text='Здесь появиться текст про Тестировщика')
    elif prof == 'developer':
        return make_response(text='Здесь появиться текст про Разработчика')
    elif prof == 'project_manager':
        return make_response(text='Здесь появиться текст про Проджект менеджера')
    elif prof == 'designer':
        return make_response(text='Здесь появиться текст про Дизайнера')
    else:
        return fallback(event)

def fallback(event):
    return make_response(
        'Извините, я Вас не поняла. Пожалуйста, попробуйте переформулировать.',
        state=event['state'][STATE_REQUEST_KEY])


def handler(event, context):
    intents = event['request'].get('nlu', {}).get('intents')
    state = event.get('state').get(STATE_REQUEST_KEY, {})
    if event['session']['new']:
        return welcome_message(event)
    elif 'start_tour' in intents:
        return start_tour(event)
    elif 'start_tour_with_prof' in intents:
        return start_tour_with_prof(event)
    elif state.get('screen') == 'start_tour' and 'start_tour_with_prof_short' in intents:
        # здесь может быть любой другой обработчик в соответсвии с интентом и статусом
        return start_tour_with_prof(event, intent_name='start_tour_with_prof_short')
    else:
        return fallback(event)
