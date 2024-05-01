sales_query = """
EVALUATE
SUMMARIZECOLUMNS(
    'Date'[Year],
    \\\"Sum\\\", round([6010_РеалТМЗ_кол], 0)
    )"""
    
cash_query = """
EVALUATE
    SUMMARIZECOLUMNS(
		'2 Проводки'[Bank_account], 'Пркл_Валюта'[Валюта],
        \\\"cash\\\", 'Balance_sheet'[cash]
    )"""
    
    
dataset_id = 'be9c90af-0400-4a50-9079-9a8ce322ac82'

sales_query_set = (dataset_id, sales_query)
cash_query_set = (dataset_id, cash_query)