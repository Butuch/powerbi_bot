dataset_id = 'be9c90af-0400-4a50-9079-9a8ce322ac82'

_sales_query = """
EVALUATE
SELECTCOLUMNS(
    SUMMARIZECOLUMNS(
        'metrics_for_bot'[Metric],
        \\\"cash\\\", 'metrics_for_bot'[Sales]
    ),
    \\\"keys\\\", 'metrics_for_bot'[Metric],
    \\\"values\\\", 'metrics_for_bot'[Sales]
)
"""
_sales_top_counter_query = """
"""
_sales_top_goods_query = """
"""
_sales_top_managers_query = """
"""
_cash_query = """
EVALUATE
SELECTCOLUMNS(
    SUMMARIZECOLUMNS(
        'metrics_for_bot'[Metric],
        \\\"cash\\\", 'metrics_for_bot'[cash_for_bi]
    ),
    \\\"keys\\\", 'metrics_for_bot'[Metric],
    \\\"values\\\", 'metrics_for_bot'[cash_for_bi]
)
"""

_inc_by_counterparty_query = """
EVALUATE
SELECTCOLUMNS(
    SUMMARIZECOLUMNS(
		'CashFlow'[Контрагент_2],
        \\\"values\\\", 'metrics_for_bot'[incoming]
	),
    \\\"keys\\\", 'CashFlow'[Контрагент_2],
    \\\"values\\\", 'metrics_for_bot'[incoming]
)
"""

_out_by_counterparty_query = """
EVALUATE
SELECTCOLUMNS(
    SUMMARIZECOLUMNS(
		'CashFlow'[Контрагент_2],
        \\\"outgoing\\\", 'metrics_for_bot'[outgoing]
	),
    \\\"keys\\\", 'CashFlow'[Контрагент_2],
    \\\"values\\\", 'metrics_for_bot'[outgoing]
)
"""
_cash_acc_query = """
EVALUATE
SELECTCOLUMNS(
    FILTER(
        SUMMARIZECOLUMNS(
            'CashFlow'[AccountNumber],
            \\\"outgoing\\\", 'metrics_for_bot'[EndingBalance]
        ),
        ROUND('metrics_for_bot'[EndingBalance], 0) <> 0
    ),
    \\\"keys\\\", 'CashFlow'[AccountNumber],
    \\\"values\\\", 'metrics_for_bot'[EndingBalance]
)
"""

sales_query_set = (dataset_id, _sales_query)
cash_query_set = (dataset_id, _cash_query)
inc_by_counterparty_query_set = (dataset_id, _inc_by_counterparty_query)
out_by_counterparty_query_set = (dataset_id, _out_by_counterparty_query)
cash_acc_query_set = (dataset_id, _cash_acc_query)
sales_top_counter_query_set = (dataset_id, _sales_top_counter_query)
sales_top_goods_query_set = (dataset_id, _sales_top_goods_query)
sales_top_managers_query_set = (dataset_id, _sales_top_managers_query)