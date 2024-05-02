from powerbi.dax_queries import (
    sales_query_set,
    cash_query_set,
    inc_by_counterparty_query_set,
    out_by_counterparty_query_set,
    cash_acc_query_set)
from powerbi.powerbi_api import execute_query_to_dict

report_sales = execute_query_to_dict(sales_query_set,
                                     sort_by=None)
report_cash = execute_query_to_dict(cash_query_set)
report_cash_inc_by_counterparty = execute_query_to_dict(inc_by_counterparty_query_set,
                                                        sort_by='value')
report_cash_out_by_counterparty = execute_query_to_dict(out_by_counterparty_query_set,
                                                        sort_by='value')
report_cash_acc = execute_query_to_dict(cash_acc_query_set,
                                        sort_by='key')

report_sales_top_counter = {
    'АО "ЖасЖибекЭнерго"': '36%',
    'ТОО "КазахЭкспорт"': '24%',
    'АО "ИнновейтСолюшнз"': '10%',
    'ТОО "ЭнергоСтройИнвест"': '7%',
    'ТОО "ИнтернетТехнологии"': '5%'
}
report_sales_top_goods = {
    'Консолидированная Power bi отчетность': '21%',
    'Внедрение программного обеспечения': '20%',
    'Консалтинг': '18%',
    'Мобильных устройства для бизнеса': '9%',
    'Бизнес-класс оборудование для касс': '7%'    
}
report_sales_top_managers = {
    'Алия Нургазинова': '24%',
    'Данияр Куанышев': '19%',
    'Айгерим Сабитова': '14%',
    'Асылжан Жумабаев': '10%',
    'Гульназ Абдрахманова': '9%'    
}