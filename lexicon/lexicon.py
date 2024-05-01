LEXICON_MAIN_MENU: dict[str, str] = {
    '/start': 'Начало взаимодействия с ботом',
    '/help': 'Справка',
    '/support': 'Обращение в тех.поддержку',
    '/contact': 'Связаться с разработчиком',
    '/info_about_user': 'Получить данные по пользователю'
}


LEXICON_COMMANDS_RU: dict[str, str] = {
    '/start': 'Выберите опцию:',
    '/help': 'Этот бот служит для отправки резюме отчётов из Power bi.\nЧтобы начать взаимодействие, нажмите /start.',
    '/support': 'Обращение в тех.поддержку',
    '/contact': '<a href="tg://user?id=567894419">Связь с разработчиком</a>',
    '/info_about_user': 'Получить данные по пользователю'
}

REPORTS_RU = {
    'sales': {
        'name': '📊 Отчёт по продажам',
        'text_get': '💹Получить краткую сводку',
        'text_notif': {
            'change': '🕒Изменить время рассылки',
            'on': '✅⏰Включить ежедневную рассылку',
            'off': '❌⏰Отключить ежедневную рассылку'
            },
        'text_link': '📈Отчет в Powerbi',
        'callbacks': {
            'get_report': 'get_report_sales',
            'notif': 'notif_sales',
            'notif_time_change': 'notif_time_change_sales',
            'get_link': 'link_sales'
            },
        'link': 'https://app.powerbi.com/view?r=eyJrIjoiNTI2NjEwYjEtNTMwNi00NWRiLThmNTAtNDZkYTM1MGMwODM2IiwidCI6ImJlMmIzZjc2LWIzNDgtNDMxYy04MjBiLWE1NjUzNTg5MDIxYiIsImMiOjl9'
        },
    'cash': {
        'name': '💰 Остаток денег',
        'text_get': '💹Получить краткую сводку',
        'text_notif': {
            'change': '🕒Изменить время рассылки',
            'on': '✅⏰Включить ежедневную рассылку',
            'off': '❌⏰Отключить ежедневную рассылку' 
            },
        'text_link': '📈Отчет в Powerbi',
        'callbacks': {
            'get_report': 'get_report_cash',
            'notif': 'notif_sales',
            'notif_time_change': 'notif_time_change_cash',
            'get_link': 'link_cash'
            },
        'link': 'https://app.powerbi.com/view?r=eyJrIjoiNTI2NjEwYjEtNTMwNi00NWRiLThmNTAtNDZkYTM1MGMwODM2IiwidCI6ImJlMmIzZjc2LWIzNDgtNDMxYy04MjBiLWE1NjUzNTg5MDIxYiIsImMiOjl'
        },
    'refresh': {
        'name': '🔄 Обновить отчеты'
    }
}

OTHER_TEXT = {
    'yes': {
        'text': 'Да',
        'callback': 'yes_refresh'
        },
    'no': {
        'text': 'Нет',
        'callback': 'no_refresh'
        },
    'sure': 'Вы уверены?\nОбновление займёт около 10 минут',
    'notif_on': '✅ Включена',
    'notif_off': '❌ Отключена',
    'reports_list': '🏠Список отчетов'
}

SYMBOLS = '💲📊✅❌🚫💰'