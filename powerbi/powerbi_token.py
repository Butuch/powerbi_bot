import requests
from dotenv import load_dotenv
import os

# Загрузка переменных из файла .env
load_dotenv()

# Получение значений переменных
POWERBI_CLIENT_ID = os.getenv("POWERBI_CLIENT_ID")
POWERBI_LOGIN = os.getenv("POWERBI_LOGIN")
POWERBI_PASS = os.getenv("POWERBI_PASS")


def _get_powerbi_access_token(client_id, username, password):
    data = {
        'grant_type': 'password',
        'scope': 'openid',
        'resource': r'https://analysis.windows.net/powerbi/api',
        'client_id': client_id,
        'username': username,
        'password': password
    }
    token = requests.post('https://login.microsoftonline.com/common/oauth2/token', data=data)
    assert token.status_code == 200, "Fail to retrieve token: {}".format(token.text)
    return token.json().get('access_token')

token_api_powerbi = _get_powerbi_access_token(POWERBI_CLIENT_ID, POWERBI_LOGIN, POWERBI_PASS)