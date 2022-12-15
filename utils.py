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


def image_list(image_ids, image_titles=[], image_descriptions=[], footer_text='Footer text'):
    items = [{'image_id': image_id} for image_id in image_ids]
    if len(image_ids) != len(image_titles) or len(image_ids) != len(image_descriptions):
        i = 0
        while i < len(items):
            items[i]['title'] = 'Title ' + str(i)
            items[i]['description'] = 'Description' + str(i)
            i += 1
        else:
            i = 0
            while i < len(items):
                items[i]['title'] = image_titles[i]
                items[i]['description'] = image_descriptions[i]
                i += 1
    return {
        'type': 'ItemsList',
        'items': items,
        "footer": {
            "text": footer_text,
        }
    }


def image_card(image_id, title, description):
    return {
        'type': 'BigImage',
        'image_id': image_id,
        'title': title,
        'description': description,
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
        button('Хочу пройти тест', hide=True),
        button('Стоп', hide=True),
    ])


def get_analyst(event):
    tts = ('Аналитик sil<[1000]> Аналитик - это специалист, который занимается выявлением'
           'бизнес-проблем, выяснению потребностей заинтересованных сторон,'
           'обоснованию решений и обеспечению проведения изменений в организации.'
           'О какой специальности рассказать еще?'
           )
    state = event['state'][STATE_REQUEST_KEY]
    state['pre_intent'] = event['request']['nlu']['intents']

    return make_response(
        text=('О какой специальности рассказать еще?'),
        tts=tts,
        card=image_gallery(image_ids=[
            '213044/63a681ed14b11c5a07f8',
            '1030494/365630c9031fddf7b64f',
        ]),
        buttons=[
            button('Аналитик'),
            button('Тестировщик'),
            button('Разработчик'),
            button('Проджект менеджер'),
            button('Дизайнер'),
            button('Хочу пройти тест', hide=True),
            button('Стоп', hide=True),
        ],
        state=state,
    )


def get_tester(event):
    tts = ('Тестировщик sil<[1000]>. Тестировщик - это тоже специалист в АйТИ без программирования, '
           'он проверяет мобильные и веб-приложения, проверяет сервисы и проектирует тесты, '
           'а главное — помогает бизнесу развиваться, а пользователям решать задачи. Тестировщику нужно '
           'уметь работать с браузерами, понимать, чем они отличаются друг от друга. '
           'А ещё быть внимательным и усидчивым, чтобы проверять продукт несколько раз '
           'и не упускать ошибки. О какой профессии рассказать еще?'
           )
    state = event['state'][STATE_REQUEST_KEY]
    state['pre_intent'] = event['request']['nlu']['intents']

    return make_response(
        text=('О какой специальности рассказать еще?'),
        tts=tts,
        card=image_gallery(image_ids=[
            '965417/da3995836be573c5105c',
            '937455/821e4711579405cb303c',
        ]),
        buttons=[
            button('Аналитик'),
            button('Тестировщик'),
            button('Разработчик'),
            button('Проджект менеджер'),
            button('Дизайнер'),
            button('Хочу пройти тест', hide=True),
            button('Стоп', hide=True),
        ],
        state=state,
    )


def get_developer(event):
    tts = ('Разработчик sil<[1000]>. Разработчик – широкий термин для группы специалистов, работа которых направлена '
           'на создание мобильных и компьютерных приложений, игр, баз данных и прочего '
           'программного обеспечения самых различных устройств. Разработчики в своей '
           'деятельности умело совмещают творческий подход и строгий язык программирования.'
           'О какой специальности рассказать еще?'
           )
    state = event['state'][STATE_REQUEST_KEY]
    state['pre_intent'] = event['request']['nlu']['intents']

    return make_response(
        text=('О какой специальности рассказать еще?'),
        tts=tts,
        card=image_gallery(image_ids=[
            '937455/90cd65c968df16b271ca',
            '1030494/93da29e28371b4fbf420',
            '937455/ff7df0037cec56949e7a',
        ]),
        buttons=[
            button('Аналитик'),
            button('Тестировщик'),
            button('Разработчик'),
            button('Проджект менеджер'),
            button('Дизайнер'),
            button('Хочу пройти тест', hide=True),
            button('Стоп', hide=True),
        ],
        state=state,
    )


def get_project_manager(event):
    tts = ('Проджект менеджер или Руководитель проектов sil<[1000]>. '
           'Проджект менеджер - это специалист, который управляет проектами. Проекты могут быть из любой сферы: '
           'АйТИ, маркетинг, строительство, музыкальные, кино-, промышленные, '
           'сельскохозяйственные и пр. Любое дело, в котором занято больше одного человека, '
           '— это уже проект. Значит, нужен человек, который организует процесс и доведет его до финала. '
           'О какой специальности рассказать еще?'
           )
    state = event['state'][STATE_REQUEST_KEY]
    state['pre_intent'] = event['request']['nlu']['intents']

    return make_response(
        text=('О какой специальности рассказать еще?'),
        tts=tts,
        card=image_gallery(image_ids=[
            '1030494/b0939295fbd1180e31c1',
            '1540737/4d2224260af3239055f2',
        ]),
        buttons=[
            button('Аналитик'),
            button('Тестировщик'),
            button('Разработчик'),
            button('Проджект менеджер'),
            button('Дизайнер'),
            button('Хочу пройти тест', hide=True),
            button('Стоп', hide=True),
        ],
        state=state,
    )


def get_designer(event):
    tts = ('Дизайнер sil<[1000]>. '
           'Дизайнер - это человек, который работает над внешним видом сайта. Он выбирает, '
           'какие элементы будут представлены на странице и в каком порядке они '
           'будут отражаться на мониторах пользователей. Например, он решает, '
           'что будет, если навести курсор мыши на определенный блок и в какой '
           'последовательности будет отображаться информация при прокрутке страницы '
           'вниз.  Веб-дизайнер думает о цветах, композиции и простоте использования '
           'сайта для пользователя.'
           'О какой специальности рассказать еще?'
           )
    state = event['state'][STATE_REQUEST_KEY]
    state['pre_intent'] = event['request']['nlu']['intents']

    return make_response(
        text=('О какой специальности рассказать еще?'),
        tts=tts,
        card=image_gallery(image_ids=[
            '1030494/2692022cbb88a5122999',
            '213044/47829b15ed70bb8d13ea',
        ]),
        buttons=[
            button('Аналитик'),
            button('Тестировщик'),
            button('Разработчик'),
            button('Проджект менеджер'),
            button('Дизайнер'),
            button('Хочу пройти тест', hide=True),
            button('Стоп', hide=True),
        ],
        state=state,
    )


def start_tour_with_prof(event, intent_name='start_tour_with_prof'):
    intent = event['request']['nlu']['intents'][intent_name]
    prof = intent['slots']['prof']['value']
    if prof == 'analyst':
        return get_analyst(event)
    elif prof == 'tester':
        return get_tester(event)
    elif prof == 'developer':
        return get_developer(event)
    elif prof == 'project_manager':
        return get_project_manager(event)
    elif prof == 'designer':
        return get_designer(event)
    else:
        return make_response(
            'Этой профессии пока нет в этом навыке, но скоро обязательно появится',
            state=event['state'][STATE_REQUEST_KEY]
        )


def what_do_you_know(event):
    return make_response(
        'Я постоянно развиваюсь, и знаю о многих профессиях. Например, могу рассказать про самые востребованные на сегодня профессии Аналитика, Тестировщика, Разработчика, Проджект менеджера, Дизайнера',
        state=event['state'][STATE_REQUEST_KEY]
    )

    # term_1 = random.choice(["Аналитик", "Тестировщик", "Разработчик", "Проджект менеджер", "Дизайнер"])
    # text = f'Я постоянно развиваюсь, на сегодяшний день я знаю о пяти профессиях. Например, рассказать про {term_1}?'
    # return make_response(text, state={
    #     'screen': 'what_do_you_know', 'prof': ''
    # }, buttons=[
    #     button('Да', hide=True),
    #     button('Нет', hide=True),
    #     button('Стоп', hide=True),
    # ])


# Тест
def welcome_test(event):
    text = ('Я могу вам предложить пройти небольшой тест, который поможет Вам определиться. '
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
    text = ('Это специалист, который занимается выявлением бизнес-проблем, '
            'выяснением потребностей заинтересованных сторон, обоснованием решений '
            'и обеспечением проведения изменений в организации. Вам нравится ?'
            )

    tts = (
        ' Аналитик sil<[1000]>. Аналитик - это специалист, который занимается выявлением бизнес-проблем, выяснением потребностей '
        'заинтересованных сторон, обоснованием решений и обеспечением проведения изменений в '
        'организации. Вам нравится ?'
        )
    return make_response(
        text='',
        tts=tts,
        card=image_card(
            image_id='1030494/b670b9ab66cb03bf63b0',
            title='Так выглядит Аналитик',
            description=text,
        ),
        state={
            'screen': 'test_q6',
        },
        buttons=[
            button('Да', hide=True),
            button('Нет', hide=True),
            button('Стоп', hide=True),
        ]
    )


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


def test_q4_1(event):
    text = ('Разбирали и ломали ли Вы в детстве игрушки?')
    return make_response(text, state={
        'screen': 'test_q4_1',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


# обработка ветки Тестировщик
def test_q4_2(event):
    text = ('Поздравляю! Вам подойдет профессия тестировщик! '
            'Хотите узнать больше о профессии? ')
    return make_response(text, state={
        'screen': 'test_q4_2',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q4_3(event):
    text = ('Это тоже специалист в АйТИ без программирования, он проверяет мобильные '
            'и веб-приложения, проверяет сервисы и проектирует тесты, а главное — помогает '
            'бизнесу развиваться, а пользователям решать задачи. Тестировщику нужно '
            'уметь работать с браузерами, понимать, чем они отличаются друг от друга. '
            'А ещё быть внимательным и усидчивым, чтобы проверять продукт несколько раз '
            'и не упускать ошибки. Вам нравиться?'
            )
    tts = ('Тестировщик sil<[1000]>. Тестировщик - это тоже специалист в АйТИ без программирования, '
           'он проверяет мобильные и веб-приложения, проверяет сервисы и проектирует тесты, '
           'а главное — помогает бизнесу развиваться, а пользователям решать задачи. Тестировщику нужно '
           'уметь работать с браузерами, понимать, чем они отличаются друг от друга. '
           'А ещё быть внимательным и усидчивым, чтобы проверять продукт несколько раз '
           'и не упускать ошибки. Вам нравиться?'
           )
    return make_response(
        text='',
        tts=tts,
        card=image_card(
            image_id='1540737/55a35da6645c941cecaf',
            title='Так выглядит Тестировщик',
            description=text,
        ),

        state={
            'screen': 'test_q4_3',
        },
        buttons=[
            button('Да', hide=True),
            button('Нет', hide=True),
            button('Стоп', hide=True),
        ])


def test_q4_4(event):
    text = ('Хотите посмотреть какие есть курсы для Тестировщиков ?')
    return make_response(text, state={
        'screen': 'test_q4_4',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q4_5(event):
    text = ('Вот такие курсы можно пройти, чтобы стать грамотным и востребованным специалистом '
            'Хотите пройти тест еще раз?'
            )
    return make_response(text, state={
        'screen': 'test_q4_5',
    }, buttons=[
        button('Курс для тестировщика 1', url='https://ya.ru'),
        button('Курс для тестировщика 2', url='https://ya.ru'),
        button('Курс для тестировщика 3', url='https://ya.ru'),
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


# обработка ветки Разработчик
def test_q4_6(event):
    text = ('Поздравляю! Вам подойдет профессия разработчик! '
            'Хотите узнать больше о профессии? ')
    return make_response(text, state={
        'screen': 'test_q4_6',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q4_7(event):
    text = ('Разработчик. Разработчик – широкий термин для группы специалистов, работа которых направлена '
            'на создание мобильных и компьютерных приложений, игр, баз данных и прочего '
            'программного обеспечения самых различных устройств. Разработчики в своей '
            'деятельности умело совмещают творческий подход и строгий язык программирования.'
            'Вам нравиться?'
            )
    tts = ('Разработчик sil<[1000]>. Разработчик – широкий термин для группы специалистов, работа которых направлена '
           'на создание мобильных и компьютерных приложений, игр, баз данных и прочего '
           'программного обеспечения самых различных устройств. Разработчики в своей '
           'деятельности умело совмещают творческий подход и строгий язык программирования.'
           'Вам нравиться?'
           )
    return make_response(
        text='',
        tts=tts,
        card=image_card(
            image_id='1030494/8bad0d6b6752762c446b',
            title='Так выглядит Разработчик',
            description=text,
        ),
        state={
            'screen': 'test_q4_7',
        },
        buttons=[
            button('Да', hide=True),
            button('Нет', hide=True),
            button('Стоп', hide=True),
        ])


def test_q4_8(event):
    text = ('Хотите посмотреть какие есть курсы для Разработчиков ?')
    return make_response(text, state={
        'screen': 'test_q4_8',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q4_9(event):
    text = ('Вот такие курсы можно пройти, чтобы стать грамотным и востребованным специалистом '
            'Хотите пройти тест еще раз?'
            )
    return make_response(text, state={
        'screen': 'test_q4_9',
    }, buttons=[
        button('Курс для разработчика 1', url='https://ya.ru'),
        button('Курс для разработчика 2', url='https://ya.ru'),
        button('Курс для разработчика 3', url='https://ya.ru'),
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


def test_q2_3(event):
    text = ('Нравится ли вам планировать свой день?')
    return make_response(text, state={
        'screen': 'test_q2_3',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q2_4(event):
    text = ('Поздравляю! Вам подойдет профессия Проджект-менеджера! Хотите узнать больше о профессии?')
    return make_response(text, state={
        'screen': 'test_q2_4',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q2_5(event):
    text = ('Проджект менеджер - это специалист, который управляет проектами. Проекты могут быть из любой сферы: '
            'АйТи, маркетинг, строительство, музыкальные, кино-, промышленные, сельскохозяйственные '
            'и пр. Любое дело, в котором занято больше одного человека, — это уже проект. Значит, '
            'нужен человек, который организует процесс и доведет его до финала. Вам нравится ?'
            )
    tts = ('Проджект менеджер или Руководитель проектов sil<[1000]>. '
           'Проджект менеджер - это специалист, который управляет проектами. Проекты могут быть из любой сферы: '
           'АйТи, маркетинг, строительство, музыкальные, кино-, промышленные, сельскохозяйственные '
           'и пр. Любое дело, в котором занято больше одного человека, — это уже проект. Значит, '
           'нужен человек, который организует процесс и доведет его до финала. Вам нравится ?'
           )
    return make_response(
        text='',
        tts=tts,
        card=image_card(
            image_id='937455/272ac9342cd8d3b8095f',
            title='Так выглядит Проджект менеджер',
            description=text,
        ),
        state={
            'screen': 'test_q2_5',
        },
        buttons=[
            button('Да', hide=True),
            button('Нет', hide=True),
            button('Стоп', hide=True),
        ])


def test_q2_6(event):
    text = ('Хотите посмотреть какие есть курсы для прожект менеджеров ?')
    return make_response(text, state={
        'screen': 'test_q2_6',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q2_7(event):
    text = ('Вот такие курсы можно пройти, чтобы стать грамотным и востребованным специалистом:'
            'Хотите пройти тест еще раз?'
            )
    return make_response(text, state={
        'screen': 'test_q2_7',
    }, buttons=[
        button('Курс для проджект менеджера 1', url='https://ya.ru'),
        button('Курс для прожект менеджера 2', url='https://ya.ru'),
        button('Курс для прожект менеджера 3', url='https://ya.ru'),
        button('Да', hide=True),
        button('Нет', hide=True),
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


def test_q2_9(event):
    text = ('Хотели бы вы научиться создавать красивый дизайн?')
    return make_response(text, state={
        'screen': 'test_q2_9',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q2_10(event):
    text = ('Поздравляю! Вам подойдет профессия Веб-дизайнер! '
            'Хотите узнать больше о профессии? ')
    return make_response(text, state={
        'screen': 'test_q2_10',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q2_11(event):
    text = ('Дизайнер. '
            'Это человек, который работает над внешним видом сайта. Он выбирает, '
            'какие элементы будут представлены на странице и в каком порядке они '
            'будут отражаться на мониторах пользователей. Например, он решает, '
            'что будет, если навести курсор мыши на определенный блок и в какой '
            'последовательности будет отображаться информация при прокрутке '
            'страницы вниз.  Веб-дизайнер думает о цветах, композиции и простоте '
            'использования сайта для пользователя. '
            'Вам нравиться?'
            )
    tts = ('Дизайнер sil<[1000]>. '
           'Это человек, который работает над внешним видом сайта. Он выбирает, '
           'какие элементы будут представлены на странице и в каком порядке они '
           'будут отражаться на мониторах пользователей. Например, он решает, '
           'что будет, если навести курсор мыши на определенный блок и в какой '
           'последовательности будет отображаться информация при прокрутке '
           'страницы вниз.  Веб-дизайнер думает о цветах, композиции и простоте '
           'использования сайта для пользователя. '
           'Вам нравиться?'
           )
    return make_response(
        text='',
        tts=tts,
        card=image_card(
            image_id='1030494/271f106942eb800d4cc5',
            title='Так выглядит Дизайнер',
            description=text,
        ),
        state={
            'screen': 'test_q2_11',
        },
        buttons=[
            button('Да', hide=True),
            button('Нет', hide=True),
            button('Стоп', hide=True),
        ])


def test_q2_12(event):
    text = ('Хотите посмотреть какие есть курсы для Дизайнеров ?')
    return make_response(text, state={
        'screen': 'test_q2_12',
    }, buttons=[
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])


def test_q2_13(event):
    text = ('Вот такие курсы можно пройти, чтобы стать грамотным и востребованным специалистом '
            'Хотите пройти тест еще раз?'
            )
    return make_response(text, state={
        'screen': 'test_q2_13',
    }, buttons=[
        button('Курс для дизайнера 1', url='https://ya.ru'),
        button('Курс для дизайнера 2', url='https://ya.ru'),
        button('Курс для дизайнера 3', url='https://ya.ru'),
        button('Да', hide=True),
        button('Нет', hide=True),
        button('Стоп', hide=True),
    ])

# *********КОНЕЦ КОДа ЮЛИ***********

