# import json
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()

# import requests


# def get_ticker(coin1='trx', coin2='usdt'):
#     response = requests.get(url=f'https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1').text
#     json_data = json.loads(response)
#     return json_data[f'{coin1}_{coin2}']['avg']

def get_ticker(coin1='tron', coin2='usd'):
    return cg.get_price(ids=coin1, vs_currencies=coin2)[coin1][coin2]


# print(get_ticker(coin1='tron', coin2='usd'))
# print(cg.get_coins_list())
#{'id': 'tether', 'symbol': 'usdt', 'name': 'Tether'}