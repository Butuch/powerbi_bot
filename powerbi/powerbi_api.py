import requests
import pandas as pd
import csv
import json


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


def execute_query(access_token: str, query_set: tuple[str, str]) -> pd.core.frame.DataFrame:
    "Executes a query to the Power BI API and returns the result as a DataFrame."
    
    dataset_id, query = query_set
    headers = {
        'Authorization': f'Bearer {access_token}',
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


def execute_query_json(access_token: str, query_set: tuple[str, str]):
    "Executes a query to the Power BI API and returns the result as a json."
    
    dataset_id, query = query_set
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = f'https://api.powerbi.com/v1.0/myorg/datasets/{dataset_id}/executeQueries'
    read_dataset = requests.post(url,
                                 data=_text_query(query),
                                 headers=headers)
    if read_dataset.status_code == 200:
        json_data = read_dataset.json()
        json_data = json_data['results'][0]['tables'][0]['rows']
        return json_data
    else:
        return {'error': f'Error: {read_dataset.status_code}'}


def execute_query_json_2(access_token: str, query_set: tuple[str, str]):
    "Executes a query to the Power BI API and returns the result as a formatted string."
    
    dataset_id, query = query_set
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = f'https://api.powerbi.com/v1.0/myorg/datasets/{dataset_id}/executeQueries'
    read_dataset = requests.post(url,
                                 data=_text_query(query),
                                 headers=headers)
    if read_dataset.status_code == 200:
        json_data = read_dataset.json()
        rows = json_data['results'][0]['tables'][0]['rows']
        columns = list(rows[0].keys())
        formatted_data = '~'.join(columns) + '\n'
        formatted_data += '\n'.join(['~'.join(map(str, row.values())) for row in rows])
        
        return formatted_data
    else:
        return f'Error: {read_dataset.status_code}'


def execute_query_csv(access_token: str, query_set: tuple[str, str]):
    "Executes a query to the Power BI API and returns the result as a csv."
    
    dataset_id, query = query_set
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = f'https://api.powerbi.com/v1.0/myorg/datasets/{dataset_id}/executeQueries'
    read_dataset = requests.post(url,
                                 data=_text_query(query),
                                 headers=headers)
    if read_dataset.status_code == 200:
        json_data = read_dataset.json()
        table_data = json_data['results'][0]['tables'][0]['rows']
        df = pd.DataFrame(table_data)
        csv_string = df.to_csv(index=False)
        return csv_string
    else:
        return f'Error: {read_dataset.status_code}'