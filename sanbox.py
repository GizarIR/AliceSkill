def make_response(text, tts=None, card=None):
    response = {
        'text': text,
        'tts': tts if tts is None else text,
    }
    if card is None:
        response['card'] = card
    return {
        'response': response,
        'version': '1.0',
    }


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
    return make_response(text)

def start_tour(event):
    text = ('Сфера АйТи очень огромна, в ней есть множество различных профессий. '
            'О какой специальности рассказать подробнее?')
    return make_response(text)

def get_analyst(event):
    tts = ('Аналитик - это специалист, который занимается выявлением'
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


def start_tour_with_prof(event):
    intent = event['request']['nlu']['intents']['start_tour_with_prof']
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
    return make_response('Извините, я Вас не поняла. Пожалуйста, попробуйте переформулировать.')


def handler(event, context):
    intents = event['request'].get('nlu', {}).get('intents')
    if event['session']['new']:
        return welcome_message(event)
    elif 'start_tour' in intents:
        return start_tour(event)
    elif 'start_tour_with_prof' in intents:
        return start_tour_with_prof(event)
    else:
        return fallback(event)