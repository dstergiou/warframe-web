import requests
from time import sleep
from requests import HTTPError
from web.settings import WARFRAME_MARKET_API, DEFAULT_SLEEP

warframe_market_standard_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'JWT',
        'Accept': 'application/json',
        'auth_type': 'header',
        'language': 'en',
        'platform': 'pc',
    }

def get_item_id_from_market(item: str) -> str:
    """
    Return the id of an item when provided the name (e.g: hikou_prime_blueprint)

    Args:
        item (str): Item name (e.g: hikou_prime_blueprint)

    Returns:
        str: ID of the item on warframe.warframe_market (e.g: '5a2feeb1c2c9e90cbdaa23d2')
    """
    try:
        response = requests.get(f'{WARFRAME_MARKET_API}/items/{item}', headers=warframe_market_standard_headers)
        sleep(DEFAULT_SLEEP)
        response.raise_for_status()
        data = response.json()
        item_id = data['payload']['item']['id']
        
        return item_id

    except HTTPError as http_err:
        print(f'HTTP Error occurred: {http_err}')
    except Exception as err:
        print(f'Error occurred: {err}')


def get_ducats_from_market(item: str) -> int:
    """
    Return the id of an item when provided the name (e.g: hikou_prime_blueprint)

    Args:
        item (str): Item name (e.g: hikou_prime_blueprint)

    Returns:
        int: Ducats value for the item (e.g 15)
    """
    ducats = 0
    try:
        response = requests.get(f'{WARFRAME_MARKET_API}/items/{item}', headers=warframe_market_standard_headers)
        sleep(DEFAULT_SLEEP)
        response.raise_for_status()
        data = response.json()
        info = data['payload']['item']['items_in_set']
        
        for line in info:
            if line['url_name'] == item:
                ducats = line.get('ducats')
        
        return ducats

    except HTTPError as http_err:
        print(f'HTTP Error occurred: {http_err}')
    except Exception as err:
        print(f'Error occurred: {err}')