from utils import *


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
    elif state.get('screen') == 'welcome_message':
        if ('welcome_test' in intents) or ('u_not' in intents):       #Ветка НЕ ЗНАЮ - идем в тест
            return welcome_test(event)
        elif ('start_prof_tour' in intents) or ('u_yes' in intents):  #Ветка ЗНАЮ - идем в тур по профессиям
            return start_tour(event)
        elif ('start_tour_with_prof_short' in intents):  #Ветка ЗНАЮ - идем в конкретную  профессию
            return start_tour_with_prof(event, intent_name='start_tour_with_prof_short')
        elif 'repeat_me' in intents:
            return welcome_message(event)
        else:
            return fallback(event)
    # Перемещаемся в Тест
    elif state.get('screen') == 'start_test':
        if 'u_yes' in intents:
            return test_q1(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return welcome_test(event)
        else:
            return fallback(event)
    # Развилка - Аналитик или Тестировщик с Разработчик
    elif state.get('screen') == 'test_q1':
        if 'u_yes' in intents:
    # ветка Аналитик
            return test_q2(event)
        elif 'u_not' in intents:
            # Уходим в ветку Юли
            return test_q2_1(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q1(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q2':
        if 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q2(event)
        else:
            return test_q3(event)
    elif state.get('screen') == 'test_q3':
        if 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q3(event)
        else:
            return test_q4(event)
    elif state.get('screen') == 'test_q4':
        if 'u_yes' in intents:
            return test_q5(event)
        elif 'u_not' in intents:
            return test_q4_1(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q4(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q5':
        if 'u_yes' in intents:
            return test_q6(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q5(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q6':
        if 'u_yes' in intents:
            return test_q7(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q6(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q7':
        if 'u_yes' in intents:
            return test_q8(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q7(event)
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
        elif 'repeat_me' in intents:
            return test_q8(event)
        else:
            return fallback(event)
    # ветка Тестировщик
    elif state.get('screen') == 'test_q4_1':
        if 'u_yes' in intents:
            return test_q4_2(event)
        elif 'u_not' in intents:
            # уходим в ветку Разработчик
            return test_q4_6(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q4_1(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q4_2':
        if 'u_yes' in intents:
            return test_q4_3(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q4_2(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q4_3':
        if 'u_yes' in intents:
            return test_q4_4(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q4_3(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q4_4':
        if 'u_yes' in intents:
            return test_q4_5(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q4_4(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q4_5':
        if 'u_yes' in intents:
            return welcome_test(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'link_to_course' in intents:
             return handler_curses(event)
        elif 'repeat_me' in intents:
            return test_q4_5(event)
        else:
            return fallback(event)
    # ветка Разработчик
    elif state.get('screen') == 'test_q4_6':
        if 'u_yes' in intents:
            return test_q4_7(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q4_6(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q4_7':
        if 'u_yes' in intents:
            return test_q4_8(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q4_7(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q4_8':
        if 'u_yes' in intents:
            return test_q4_9(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q4_8(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q4_9':
        if 'u_yes' in intents:
            return welcome_test(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'link_to_course' in intents:
             return handler_curses(event)
        elif 'repeat_me' in intents:
            return test_q4_9(event)
        else:
            return fallback(event)
    #*********КОД ЮЛИ******************
    elif state.get('screen') == 'test_q2_1':
        if 'u_yes' in intents:
            return test_q2_2(event)
        elif 'u_not' in intents:
            return test_q2_8(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q2_1(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q2_2':
        if 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q2_2(event)
        else:
            return test_q2_3(event)
    elif state.get('screen') == 'test_q2_3':
        if 'u_yes' in intents:
            return test_q2_4(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q2_3(event)
        else:
            return fallback(event)

    elif state.get('screen') == 'test_q2_4':
        if 'u_yes' in intents:
            return test_q2_5(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q2_4(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q2_5':
        if 'u_yes' in intents:
            return test_q2_6(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q2_5(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q2_6':
        if 'u_yes' in intents:
            return test_q2_7(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q2_6(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q2_7':
        if 'u_yes' in intents:
            return welcome_test(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q2_7(event)
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
        elif 'repeat_me' in intents:
            return test_q2_8(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q2_9':
        if 'u_yes' in intents:
            return test_q2_10(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q2_9(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q2_10':
        if 'u_yes' in intents:
            return test_q2_11(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q2_10(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q2_11':
        if 'u_yes' in intents:
            return test_q2_12(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q2_11(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q2_12':
        if 'u_yes' in intents:
            return test_q2_13(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q2_12(event)
        else:
            return fallback(event)
    elif state.get('screen') == 'test_q2_13':
        if 'u_yes' in intents:
            return welcome_test(event)
        elif 'u_not' in intents:
            return start_tour(event)
        elif 'u_stop' in intents:
            return goodbye(event)
        elif 'repeat_me' in intents:
            return test_q2_13(event)
        elif 'link_to_course' in intents:
             return handler_curses(event)
        else:
            return fallback(event)
    #*********КОНЕЦ КОДа ЮЛИ***********
    # Ветка ЗНАЮ
    # elif 'start_prof_tour' in intents:
    #     return start_tour(event)
    elif 'start_tour_with_prof' in intents:
        return start_tour_with_prof(event)
    elif state.get('screen') == 'start_tour'  and 'start_tour_with_prof_short' in intents:
        return start_tour_with_prof(event, intent_name='start_tour_with_prof_short')
    # elif state.get('screen') == 'start_tour'  and 'repeat_me' in intents:
    #     return start_tour_with_prof(event, intent_name='start_tour_with_prof_short', prof=state.get('pre_prof'))
    elif state.get('screen') == 'start_tour'  and 'repeat_me' in intents:
        event['request']['nlu']['intents']['start_tour_with_prof_short'] = state.get('pre_intent')
        return start_tour_with_prof(event, intent_name='start_tour_with_prof_short')
    elif state.get('screen') == 'start_tour' and 'want_test' in intents:
        return welcome_test(event)
    elif state.get('screen') == 'start_tour' and 'u_not' in intents:
        return goodbye(event)
    # Обработка неизвестных ответов и вопросов пользователля
    else:
        if 'u_stop' in intents:
            return goodbye(event)
        else:
            return fallback(event)
