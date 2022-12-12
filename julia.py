

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
            'IT, маркетинг, строительство, музыкальные, кино-, промышленные, сельскохозяйственные '
            'и пр. Любое дело, в котором занято больше одного человека, — это уже проект. Значит, '
            'нужен человек, который организует процесс и доведет его до финала. Вам нравится ?'
            )
    tts = ('Проджект менеджер или Руководитель проектов sil<[1000]>. '
           'Проджект менеджер - это специалист, который управляет проектами. Проекты могут быть из любой сферы: '
           'IT, маркетинг, строительство, музыкальные, кино-, промышленные, сельскохозяйственные '
           'и пр. Любое дело, в котором занято больше одного человека, — это уже проект. Значит, '
           'нужен человек, который организует процесс и доведет его до финала. Вам нравится ?'
           )
    return make_response(
        text,
        tts=tts,
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

    # *********КОНЕЦ КОДа ЮЛИ***********


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

    elif state.get('screen') == 'test_q2_2':
        if 'u_stop' in intents:
            return goodbye(event)
        else:
            return test_q2_3(event)

    elif state.get('screen') == 'test_q2_3':
        if 'u_yes' in intents:
            return test_q2_4(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)

    elif state.get('screen') == 'test_q2_4':
        if 'u_yes' in intents:
            return test_q2_5(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)

    elif state.get('screen') == 'test_q2_5':
        if 'u_yes' in intents:
            return test_q2_6(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)

    elif state.get('screen') == 'test_q2_6':
        if 'u_yes' in intents:
            return test_q2_7(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)

    elif state.get('screen') == 'test_q2_7':
        if 'u_yes' in intents:
            return welcome_test(event)
        elif 'u_not' in intents:
            #должен увидеть прощание
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
            #строка 522 и 523 вроде как лишние
        elif 'link_to_course' in intents:
            return handler_curses(event)
        else:
            return fallback(event)                                           

    elif state.get('screen') == 'test_q2_8':
        if 'u_yes' in intents:
            return test_q2_9(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)    
              
    # *********КОНЕЦ КОДа ЮЛИ***********