LEXICON_MAIN_MENU: dict[str, str] = {
    '/start': 'Начало взаимодействия с ботом',
    '/help': 'Справка',
    '/contact': 'Связаться с разработчиком'
}


LEXICON_COMMANDS_RU: dict[str, str] = {
    '/start': 'Выберите опцию:',
    '/help': 'Бот служит для отправки сводки отчётов из Power bi.\nРаботает в демонстрационном режиме.\nЧтобы начать взаимодействие, нажмите /start.',
    '/support': 'Обращение в тех.поддержку',
    '/contact': '<a href="tg://user?id=567894419">Связь с разработчиком</a>',
    '/info_about_user': 'Получить данные по пользователю'
}

REPORTS_RU = {
    'sales': {
        'name': '📊 Отчёт по выручке',
        'text_get': '📈 Получить краткую сводку',
        'text_notif': {
            'change': '🕒 Изменить время рассылки',
            'on': '⏰Включить ежедневную рассылку',
            'off': 'Отключить ежедневную рассылку'
            },
        'text_link': '🔍 Отчет в Powerbi',
        'callbacks': {
            'get_report': 'get_report_sales',
            'notif': 'notif_sales',
            'notif_time_change': 'notif_time_change_sales',
            'get_link': 'link_sales'
            },
        'link': 'https://app.powerbi.com/view?r=eyJrIjoiNTI2NjEwYjEtNTMwNi00NWRiLThmNTAtNDZkYTM1MGMwODM2IiwidCI6ImJlMmIzZjc2LWIzNDgtNDMxYy04MjBiLWE1NjUzNTg5MDIxYiIsImMiOjl9'
        },
    'sales_top_counter': {
        'name': '🏆 Топ 5 Покупателей',
        'callback': 'top_counter'
            },
    'sales_top_goods': {
        'name': '🛍️ Топ 5 Товаров и Услуг',
        'callback': 'top_goods'
            },
    'sales_top_managers': {
        'name': '👔 Топ 5 Менеджеров',
        'callback': 'top_managers'
            },
    'cash': {
        'name': '💰 Остаток денег',
        'text_get': '📈 Получить краткую сводку',
        'text_notif': {
            'change': '🕒 Изменить время рассылки',
            'on': '⏰ Включить ежедневную рассылку',
            'off': 'Отключить ежедневную рассылку' 
            },
        'text_link': '🔍 Отчет в Powerbi',
        'callbacks': {
            'get_report': 'get_report_cash',
            'notif': 'notif_cash',
            'notif_time_change': 'notif_time_change_cash',
            'get_link': 'link_cash'
            },
        'link': 'https://app.powerbi.com/view?r=eyJrIjoiNTI2NjEwYjEtNTMwNi00NWRiLThmNTAtNDZkYTM1MGMwODM2IiwidCI6ImJlMmIzZjc2LWIzNDgtNDMxYy04MjBiLWE1NjUzNTg5MDIxYiIsImMiOjl9'
        },
    'cash_acc': {
        'name': '💰 Остаток денег по счетам',
        'callback': 'get_cash_by_acc'
            },
    'cash_inc_counter': {
        'name': '🔼 Поступление по контрагентам',
        'callback': 'get_cash_inc_by_counter'
            },
    'cash_out_counter': {
        'name': '🔽 Выбытие по контрагентам',
        'callback': 'get_cash_out_by_counter'
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
    'sure': 'Обновление продлится около 10 минут\nПродолжаем?',
    'notif_on': '✅ Включена',
    'notif_off': '❌ Отключена',
    'reports_list': '🏠 Главное меню'
}

SYMBOLS = '💲📊✅❌🚫💰'