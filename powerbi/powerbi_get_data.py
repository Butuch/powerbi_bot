from .powerbi_token import token_api_powerbi
from .dax_queries import sales_query_set, cash_query_set
from .powerbi_api import execute_query_json_2

report_sales = execute_query_json_2(token_api_powerbi, sales_query_set)
report_cash = execute_query_json_2(token_api_powerbi, cash_query_set)