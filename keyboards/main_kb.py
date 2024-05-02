import sys
sys.path.append('.')

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import REPORTS_RU

btn_report_sales = KeyboardButton(text=REPORTS_RU['sales']['name'])
btn_report_cash = KeyboardButton(text=REPORTS_RU['cash']['name'])
refresh_reports = KeyboardButton(text=REPORTS_RU['refresh']['name'])

# reports_kb = ReplyKeyboardMarkup(
#     keyboard=[[btn_report_sales],
#               [btn_report_cash]],
#     resize_keyboard=True
# )

reports_kb_builder = ReplyKeyboardBuilder()

reports_kb_builder.row(btn_report_cash, btn_report_sales, refresh_reports, width=2)

reports_kb: ReplyKeyboardMarkup = reports_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)