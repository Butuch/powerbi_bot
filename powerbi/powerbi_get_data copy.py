import pandas as pd

from .dax_queries import sales_query_set, cash_query_set
from .powerbi_api import execute_query_json_2, execute_query

pre_report_sales = execute_query(sales_query_set)
pre_report_cash = execute_query(cash_query_set)

# Transform Sales
report_sales = pre_report_sales.copy()
report_sales = report_sales.rename(columns={
    'Date[Year]': 'Год',
    '[Sum]': 'Сумма'
    }
)
report_sales['Сумма'] = report_sales['Сумма'].map(lambda x: '{:,.0f}'.format(x).replace(',', ' '))
report_sales = report_sales.to_string(index=False)

# Transform Cash
report_cash = pre_report_cash.copy()
report_cash = report_cash.rename(columns={
    '2 Проводки[Bank_account]': 'Счет',
    'Пркл_Валюта[Валюта]': 'currency',
    '[cash]': 'amount'
    }
                           )
report_cash = report_cash.pivot_table(
    index='Счет',
    columns='currency',
    values='amount',
    aggfunc='sum'
).rename_axis(columns=None).reset_index()

report_cash[['KZT', 'EUR', 'USD']] = report_cash[['KZT', 'EUR', 'USD']].apply(lambda x: x.apply(lambda y: '{:,.0f}'.format(y).replace(',', ' ')))

report_cash = report_cash.to_string(index=False)