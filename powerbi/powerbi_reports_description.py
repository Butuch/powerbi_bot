import sys
sys.path.append('.')
from lexicon.lexicon import OTHER_TEXT

reports_description = {
    'sales': {
        '<b>Обновлено</b>': '25.04.24 04:00',
        '<b>Описание</b>': 'Продажи за предыдущий день',
        '<b>Рассылка</b>': OTHER_TEXT['notif_off']
    },
    'cash': {
        '<b>Обновлено</b>': '28.04.24 03:00',
        '<b>Описание</b>': 'Остаток денег на дату актуализации',
        '<b>Рассылка</b>': OTHER_TEXT['notif_off']
    }
}