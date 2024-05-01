import sys
sys.path.append('.')

from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           Message, CallbackQuery)

from lexicon.lexicon import REPORTS_RU, OTHER_TEXT

btn_back = InlineKeyboardButton(
    text=OTHER_TEXT['reports_list'],
    callback_data='back'
)

# Sales
btn_get_report_sales = InlineKeyboardButton(
    text=REPORTS_RU['sales']['text_get'],
    callback_data=REPORTS_RU['sales']['callbacks']['get_report']
)

btn_notif_on_sales = InlineKeyboardButton(
    text=REPORTS_RU['sales']['text_notif']['on'],
    callback_data=REPORTS_RU['sales']['callbacks']['notif']
)

btn_notif_off_sales = InlineKeyboardButton(
    text=REPORTS_RU['sales']['text_notif']['off'],
    callback_data=REPORTS_RU['sales']['callbacks']['notif']
)

btn_notif_cnahge_sales = InlineKeyboardButton(
    text=REPORTS_RU['sales']['text_notif']['change'],
    callback_data=REPORTS_RU['sales']['callbacks']['notif_time_change']
)

btn_link_powerbi_sales = InlineKeyboardButton(
    text=REPORTS_RU['sales']['text_link'],
    url=REPORTS_RU['sales']['link']
)

inline_reports_on_keyboard_sales = InlineKeyboardMarkup(
    inline_keyboard=[[btn_get_report_sales],
                     [btn_notif_on_sales],
                     [btn_link_powerbi_sales],
                     [btn_back]]
)

inline_reports_off_keyboard_sales = InlineKeyboardMarkup(
    inline_keyboard=[[btn_get_report_sales],
                     [btn_notif_cnahge_sales],
                     [btn_notif_off_sales],
                     [btn_link_powerbi_sales],
                     [btn_back]]
)

# Cash
btn_get_report_cash = InlineKeyboardButton(
    text=REPORTS_RU['cash']['text_get'],
    callback_data=REPORTS_RU['cash']['callbacks']['get_report']
)

btn_notif_on_cash = InlineKeyboardButton(
    text=REPORTS_RU['cash']['text_notif']['on'],
    callback_data=REPORTS_RU['cash']['callbacks']['notif']
)

btn_notif_off_cash = InlineKeyboardButton(
    text=REPORTS_RU['cash']['text_notif']['off'],
    callback_data=REPORTS_RU['cash']['callbacks']['notif']
)

btn_notif_cnahge_cash = InlineKeyboardButton(
    text=REPORTS_RU['cash']['text_notif']['change'],
    callback_data=REPORTS_RU['cash']['callbacks']['notif_time_change']
)

btn_link_powerbi_cash = InlineKeyboardButton(
    text=REPORTS_RU['cash']['text_link'],
    url=REPORTS_RU['cash']['link']
)

inline_reports_on_keyboard_cash = InlineKeyboardMarkup(
    inline_keyboard=[[btn_get_report_cash],
                     [btn_notif_on_cash],
                     [btn_link_powerbi_cash],
                     [btn_back]]
)

inline_reports_off_keyboard_cash = InlineKeyboardMarkup(
    inline_keyboard=[[btn_get_report_cash],
                     [btn_notif_off_cash],
                     [btn_notif_cnahge_cash],
                     [btn_link_powerbi_cash],
                     [btn_back]]
)

# refresh
btn_yes_refresh = InlineKeyboardButton(
    text=OTHER_TEXT['yes']['text'],
    callback_data=OTHER_TEXT['yes']['callback']
)

btn_no_refresh = InlineKeyboardButton(
    text=OTHER_TEXT['no']['text'],
    callback_data=OTHER_TEXT['no']['callback']
)

inline_refresh_keyboard_yes_no = InlineKeyboardMarkup(
    inline_keyboard=[[btn_yes_refresh, btn_no_refresh]]
)