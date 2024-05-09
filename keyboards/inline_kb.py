import sys
sys.path.append('.')

from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           Message, CallbackQuery)

from lexicon.lexicon import REPORTS_RU, OTHER_TEXT

_btn_back = InlineKeyboardButton(
    text=OTHER_TEXT['reports_list'],
    callback_data='back'
)

######################### SALES ####################################
# get report sales
_btn_get_report_sales = InlineKeyboardButton(
    text=REPORTS_RU['sales']['text_get'],
    callback_data=REPORTS_RU['sales']['callbacks']['get_report']
)

# button get report sales top 10 counter
_btn_get_report_sales_top_counter = InlineKeyboardButton(
    text=REPORTS_RU['sales_top_counter']['name'],
    callback_data=REPORTS_RU['sales_top_counter']['callback']
)
# button get report sales top 10 goods
_btn_get_report_sales_top_goods = InlineKeyboardButton(
    text=REPORTS_RU['sales_top_goods']['name'],
    callback_data=REPORTS_RU['sales_top_goods']['callback']
)
# button get report sales top 10 managers
_btn_get_report_sales_top_managers = InlineKeyboardButton(
    text=REPORTS_RU['sales_top_managers']['name'],
    callback_data=REPORTS_RU['sales_top_managers']['callback']
)
# buttons assembly
inline_reports_sales_details = InlineKeyboardMarkup(
    inline_keyboard=[[_btn_get_report_sales_top_counter],
                     [_btn_get_report_sales_top_goods],
                     [_btn_get_report_sales_top_managers],
                     [_btn_back]]
)
# notification is on
_btn_notif_on_sales = InlineKeyboardButton(
    text=REPORTS_RU['sales']['text_notif']['on'],
    callback_data=REPORTS_RU['sales']['callbacks']['notif']
)

# notification is off
_btn_notif_off_sales = InlineKeyboardButton(
    text=REPORTS_RU['sales']['text_notif']['off'],
    callback_data=REPORTS_RU['sales']['callbacks']['notif']
)

# change time notification
_btn_notif_cnahge_sales = InlineKeyboardButton(
    text=REPORTS_RU['sales']['text_notif']['change'],
    callback_data=REPORTS_RU['sales']['callbacks']['notif_time_change']
)

# get link power bi
_btn_link_powerbi_sales = InlineKeyboardButton(
    text=REPORTS_RU['sales']['text_link'],
    url=REPORTS_RU['sales']['link']
)

# inline keyboard with nofication is on
inline_reports_on_keyboard_sales = InlineKeyboardMarkup(
    inline_keyboard=[[_btn_get_report_sales],
                     [_btn_notif_on_sales],
                     [_btn_link_powerbi_sales],
                     [_btn_back]]
)

# inline keyboard with nofication is off
inline_reports_off_keyboard_sales = InlineKeyboardMarkup(
    inline_keyboard=[[_btn_get_report_sales],
                     [_btn_notif_cnahge_sales],
                     [_btn_notif_off_sales],
                     [_btn_link_powerbi_sales],
                     [_btn_back]]
)

######################### CASH ####################################
# get report cash
_btn_get_report_cash = InlineKeyboardButton(
    text=REPORTS_RU['cash']['text_get'],
    callback_data=REPORTS_RU['cash']['callbacks']['get_report']
)

# button get report cash by accounts
_btn_get_report_cash_acc = InlineKeyboardButton(
    text=REPORTS_RU['cash_acc']['name'],
    callback_data=REPORTS_RU['cash_acc']['callback']
)
# button get report cash income by counter
_btn_get_report_cash_inc_counter = InlineKeyboardButton(
    text=REPORTS_RU['cash_inc_counter']['name'],
    callback_data=REPORTS_RU['cash_inc_counter']['callback']
)
# button get report cash out by accounts
_btn_get_report_cash_out_counter = InlineKeyboardButton(
    text=REPORTS_RU['cash_out_counter']['name'],
    callback_data=REPORTS_RU['cash_out_counter']['callback']
)
# buttons assembly
inline_reports_cash_details = InlineKeyboardMarkup(
    inline_keyboard=[[_btn_get_report_cash_acc],
                     [_btn_get_report_cash_inc_counter],
                     [_btn_get_report_cash_out_counter],
                     [_btn_back]]
)

# notification is on
_btn_notif_on_cash = InlineKeyboardButton(
    text=REPORTS_RU['cash']['text_notif']['on'],
    callback_data=REPORTS_RU['cash']['callbacks']['notif']
)

# notification is off
_btn_notif_off_cash = InlineKeyboardButton(
    text=REPORTS_RU['cash']['text_notif']['off'],
    callback_data=REPORTS_RU['cash']['callbacks']['notif']
)

# change time notification
_btn_notif_cnahge_cash = InlineKeyboardButton(
    text=REPORTS_RU['cash']['text_notif']['change'],
    callback_data=REPORTS_RU['cash']['callbacks']['notif_time_change']
)

# get link power bi
_btn_link_powerbi_cash = InlineKeyboardButton(
    text=REPORTS_RU['cash']['text_link'],
    url=REPORTS_RU['cash']['link']
)

# inline keyboard with nofication is on
inline_reports_on_keyboard_cash = InlineKeyboardMarkup(
    inline_keyboard=[[_btn_get_report_cash],
                     [_btn_notif_on_cash],
                     [_btn_link_powerbi_cash],
                     [_btn_back]]
)

# inline keyboard with nofication is off
inline_reports_off_keyboard_cash = InlineKeyboardMarkup(
    inline_keyboard=[[_btn_get_report_cash],
                     [_btn_notif_cnahge_cash],
                     [_btn_notif_off_cash],
                     [_btn_link_powerbi_cash],
                     [_btn_back]]
)

######################### OTHER ####################################
# refresh
_btn_yes_refresh = InlineKeyboardButton(
    text=OTHER_TEXT['yes']['text'],
    callback_data=OTHER_TEXT['yes']['callback']
)

# refresh report
_btn_no_refresh = InlineKeyboardButton(
    text=OTHER_TEXT['no']['text'],
    callback_data=OTHER_TEXT['no']['callback']
)

# refresh buttons with yes and no
inline_refresh_keyboard_yes_no = InlineKeyboardMarkup(
    inline_keyboard=[[_btn_yes_refresh, _btn_no_refresh]]
)