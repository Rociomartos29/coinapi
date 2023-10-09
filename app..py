import requests


apikey = 'C2A0C4FB-F8FB-4CA1-9476-FBC27D919536'
server = 'https://rest.coinapi.io'
endpoint = '/v1/assets?filter_asset_id=EUR;BTC;USD;ETH'

url = server + endpoint

headers = {
    'X-CoinAPI-Key': apikey
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    json_response = response.json()

    for coin in json_response:
        id = coin.get('asset_id')
        # if (id in ['BTC', 'USD', 'EUR', 'ETH']):
        #     print(id, '-', coin.get('name'), coin.get('type_is_crypto'))
        print(id, '-', coin.get('name'), coin.get('type_is_crypto'))
else:
    print('Algo no ha ido bien. Error ', response.status_code, response.reason)