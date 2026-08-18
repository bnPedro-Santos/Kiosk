import requests

url = (
'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
)

resp = requests.get(url)
data = resp.json()

def get_infos(conversao):
    if resp.status_code == 200:
        seta = '^' if float(data[conversao]['pctChange']) >= 0 else 'v'

        return (
        f'{conversao[:3]}: {float(data[conversao]['bid']):.2f},'
        f'{seta} ({float(data[conversao]['pctChange']):.2f}%)'
        )



print(get_infos('USDBRL'))
print(get_infos('EURBRL'))
print(get_infos('BTCBRL'))
