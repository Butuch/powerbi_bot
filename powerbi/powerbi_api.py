import requests
import pandas as pd
import json

from powerbi.powerbi_token import token_api_powerbi
from powerbi.dax_queries import sales_query_set, cash_query_set


def _get_powerbi_datasets(access_token):
    "Get datasets list"
    
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = 'https://api.powerbi.com/v1.0/myorg/datasets'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        dataframe = pd.DataFrame(data['value'])
        return dataframe
    else:
        print("Failed to get Power BI data:", response.text)
        return None


def _text_query(dax_query):
    "Formatting dax query to query for api"
    
    api_query = '''
    {
        "queries": [
            {
                "query": "''' + dax_query + '''"
            }
        ]
    }
    '''
    api_query = api_query.encode('utf-8')
    return api_query


# Executes a query to the Power BI API and returns the result as a DataFrame
def execute_query(query_set: tuple[str, str]) -> pd.core.frame.DataFrame:
    "Executes a query to the Power BI API and returns the result as a DataFrame."
    
    dataset_id, query = query_set
    headers = {
        'Authorization': f'Bearer {token_api_powerbi}',
        'Content-Type': 'application/json'
    }
    url = f'https://api.powerbi.com/v1.0/myorg/datasets/{dataset_id}/executeQueries'
    read_dataset = requests.post(url,
                                 data=_text_query(query),
                                 headers=headers)
    if read_dataset.status_code == 200:
        df = json.loads(read_dataset.text)
        table = pd.DataFrame(df['results'][0]['tables'][0]['rows'])
        return table
    else:
        return pd.DataFrame() # f'Error: {read_dataset.status_code}'



def execute_query_to_dict(query_set: tuple[str, str], sort_by: str | None = None) -> dict:
    "Executes a query to the Power BI API and returns the result as a dict"
    dataset_id, query = query_set
    headers = {
        'Authorization': f'Bearer {token_api_powerbi}',
        'Content-Type': 'application/json'
    }
    url = f'https://api.powerbi.com/v1.0/myorg/datasets/{dataset_id}/executeQueries'
    read_dataset = requests.post(url,
                                 data=_text_query(query),
                                 headers=headers)
    if read_dataset.status_code == 200:
        json_data = read_dataset.json()
        rows = json_data['results'][0]['tables'][0]['rows']
        formatted_data = {}
        for row in rows:
            metric = row['[keys]']
            value = int(row['[values]'])
            formatted_data[metric] = value
            
        if sort_by == 'key':
            formatted_data = dict(sorted(formatted_data.items(), key=lambda item: item[0]))
        elif sort_by == 'value':
            formatted_data = dict(sorted(formatted_data.items(), key=lambda item: item[1], reverse=True))
        elif sort_by is None:
            pass
        else:
            raise ValueError("Invalid value for 'sort_by'. Use 'key', 'value', or None.")
        
        return formatted_data
    else:
        return f'Error: {read_dataset.status_code}'