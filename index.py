STATE_REQUEST_KEY = 'session'
STATE_RESPONSE_KEY = 'session_state'


def make_response(text, tts=None, card=None, state=None, buttons=None, end_session=False):
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
    if end_session:
        response['end_session'] = end_session
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


# НАЧАЛО диалога
def welcome_message(event):
    text = ('Добро пожаловать, тут я могу помочь вам найти для себя новую профессию. '
            'Расскажу о самых интересных и востребованных IT профессий. '
            'Вы знаете какое направление вас интересует?')
    return make_response(text, state={
        'screen': 'welcome_message',
    }, buttons=[
        button('Знаю', hide=True),
        button('Не знаю', hide=True),
    ])


# Рассказ о профессиях ( и Сценарий нет)
def start_tour(event):
    text = ('Сфера АйТи очень огромна, в ней есть множество различных профессий. '
            'О какой специальности рассказать подробнее?')
    return make_response(text, state={
        'screen': 'start_tour',
    }, buttons=[
        button('Аналитик'),
        button('Тестировщик'),
        button('Разработчик'),
        button('Проджект менеджер'),
        button('Дизайнер'),
        button('Стоп', hide=True),
    ])


def get_analyst(event):
    tts = ('Аналитик sil<[1000]> Аналитик - это специалист, который занимается выявлением'
           'бизнес-проблем, выяснению потребностей заинтересованных сторон,'
           'обоснованию решений и обеспечению проведения изменений в организации.'
           'О какой специальности рассказать еще?'
           )
    return make_response(
        text=('О какой специальности рассказать еще?'),
        tts=tts,
        card=image_gallery(image_ids=[
            '965417/c21764e6199631467555',
            '1540737/e958a13e0e9801227c06',
        ]),
        buttons=[
            button('Аналитик'),
            button('Тестировщик'),
            button('Разработчик'),
            button('Проджект менеджер'),
            button('Дизайнер'),
            button('Стоп', hide=True),
        ],
        state=event['state'][STATE_REQUEST_KEY],
    )


def get_tester(event):
    pass


def get_developer(event):
    pass


def get_project_manager(event):
    pass


def get_designer(event):
    pass


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


# Тест
def welcome_test(event):
    text = ('Я могу вам предложить пройти небольшой тест, который может вам определиться. '
            'Запускаем?')
    return make_response(text, state={
        'screen': 'start_test',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q1(event):
    text = ('Получаете ли вы удовольствие, решая различные головоломки?')
    return make_response(text, state={
        'screen': 'test_q1',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q2(event):
    text = ('Выберите суперсилу: становиться невидимым или уметь летать?')
    return make_response(text, state={
        'screen': 'test_q2',
    }, buttons=[
        button('Становиться невидимым', hide=True),
        button('Уметь летать', hide=True),
        button('Стоп', hide=True),
    ])


def test_q3(event):
    text = ('За какую зарплату вы готовы мыть все окна в Москве, больше или меньше 100 тысяч рублей?')
    return make_response(text, state={
        'screen': 'test_q3',
    }, buttons=[
        button('Меньше ста тысяч рублей', hide=True),
        button('Больше ста тысяч рублей', hide=True),
        button('Стоп', hide=True),
    ])


# развилка на Аналитика и Тестировщика с Разработчиком
def test_q4(event):
    text = ('Нравится ли вам общаться с людьми?')
    return make_response(text, state={
        'screen': 'test_q4',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


# ветка Аналитик
def test_q5(event):
    text = ('Поздравляю! Вам подойдет профессия Аналитика! Хотите узнать больше о профессии?')
    return make_response(text, state={
        'screen': 'test_q5',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q6(event):
    text = ('Это специалист, который занимается выявлением бизнес-проблем, выяснением потребностей '
            'заинтересованных сторон, обоснованием решений и обеспечением проведения изменений в '
            'организации. Вам нравится ?'
            )
    tts = (
        ' Аналитик sil<[1000]>. Аналитик - это специалист, который занимается выявлением бизнес-проблем, выяснением потребностей '
        'заинтересованных сторон, обоснованием решений и обеспечением проведения изменений в '
        'организации. Вам нравится ?'
        )
    return make_response(
        text,
        tts=tts,
        state={
            'screen': 'test_q6',
        },
        buttons=[
            button('Да', hide=True),
            button('Нет', hide=True),
            button('Стоп', hide=True),
        ])


def test_q7(event):
    text = ('Хотите посмотреть какие есть курсы для Аналитиков ?')
    return make_response(text, state={
        'screen': 'test_q7',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q8(event):
    text = ('Вот такие курсы можно пройти, чтобы стать грамотным и востребованным специалистом '
            'Хотите пройти тест еще раз?'
            )
    return make_response(text, state={
        'screen': 'test_q8',
    }, buttons=[
        button('Курс для аналитика 1', url='https://ya.ru'),
        button('Курс для аналитика 2', url='https://ya.ru'),
        button('Курс для аналитика 3', url='https://ya.ru'),
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


# *********КОД ЮЛИ******************
def test_q2_1(event):
    text = ('Готовы ли вы лидировать в команде?')
    return make_response(text, state={
        'screen': 'test_q2_1',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q2_2(event):
    text = ('Если бы вы стали деревом, то каким?')
    return make_response(text, state={
        'screen': 'test_q2_2',
    }, buttons=[
        button('Дуб', hide=True),
        button('Береза', hide=True),
        button('Стоп', hide=True),
    ])


def test_q2_8(event):
    text = ('Рисуете ли вы в воображении места, куда хотите отправиться?')
    return make_response(text, state={
        'screen': 'test_q2_8',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


# *********КОНЕЦ КОДа ЮЛИ***********


# Специфические обработки запросов
def fallback(event):
    return make_response(
        'Извините, я Вас не поняла. Пожалуйста, попробуйте переформулировать.',
        state=event['state'][STATE_REQUEST_KEY])


def handler_curses(event):
    text = ('Отличный выбор курса. Хотите пройти тест еще раз?')
    return make_response(
        text,
        state=event['state'][STATE_REQUEST_KEY],
        buttons=[
            button('Да', hide=True),
            button('Нет', hide=True),
            button('Стоп', hide=True),
        ])


def goodbye(event):
    return make_response(
        'Было приятно поболтать! До новых встреч!',
        state=None,
        end_session=True)


# Основной обработчик
def handler(event, context):
    intents = event['request'].get('nlu', {}).get('intents')
    state = event.get('state').get(STATE_REQUEST_KEY, {})
    if event['session']['new']:
        return welcome_message(event)
    # Ветка НЕ ЗНАЮ
    elif 'welcome_test' in intents:
        return welcome_test(event)
    # Перемещаемся в Тест
    elif state.get('screen') == 'start_test':
        if 'u_yes' in intents:
            return test_q1(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)
    # Развилка - Аналитик или Тестировщик с Разработчиком
    elif state.get('screen') == 'test_q1':
        if 'u_yes' in intents:
            return test_q2(event)
        elif 'u_not' in intents:
            # Уходим в ветку Юли
            return test_q2_1(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q2':
        if 'u_stop' in intents:
            return goodbye(event)
        else:
            return test_q3(event)
    elif state.get('screen') == 'test_q3':
        if 'u_stop' in intents:
            return goodbye(event)
        else:
            return test_q4(event)
    elif state.get('screen') == 'test_q4':
        if 'u_yes' in intents:
            return test_q5(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q5':
        if 'u_yes' in intents:
            return test_q6(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q6':
        if 'u_yes' in intents:
            return test_q7(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q7':
        if 'u_yes' in intents:
            return test_q8(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q8':
        if 'u_yes' in intents:
            return welcome_test(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'link_to_course' in intents:
            return handler_curses(event)
        else:
            return fallback(event)
    # *********КОД ЮЛИ******************
    elif state.get('screen') == 'test_q2_1':
        if 'u_yes' in intents:
            return test_q2_2(event)
        elif 'u_not' in intents:
            return test_q2_8(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)
    # *********КОНЕЦ КОДа ЮЛИ***********
    # Ветка ЗНАЮ
    elif 'start_prof_tour' in intents:
        return start_tour(event)
    elif 'start_tour_with_prof' in intents:
        return start_tour_with_prof(event)
    elif state.get('screen') == 'start_tour' and 'start_tour_with_prof_short' in intents:
        return start_tour_with_prof(event, intent_name='start_tour_with_prof_short')
    elif state.get('screen') == 'start_tour' and 'u_not' in intents:
        return goodbye(event)
    # Обработка неизвестных ответов и вопросов пользователля
    else:
        if 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)
