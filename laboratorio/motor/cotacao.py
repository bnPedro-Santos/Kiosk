import requests

def buscar_cotacoes():
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
    
    try:
        resp = requests.get(url)
        
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"Erro na Internet: A API respondeu com o código {resp.status_code}")
            return None
            
    except requests.exceptions.RequestException as erro:
        print(f"Erro Crítico de Conexão: Falha ao acessar a rede. ({erro})")
        return None



def get_info_moeda(dados, conversao):
    if not dados or conversao not in dados:
        return None
        
    dados_moeda = dados[conversao]
    
    pct_change = float(dados_moeda['pctChange'])
    bid = float(dados_moeda['bid'])
    
    tendencia = 'subiu' if pct_change >= 0 else 'caiu'
    
    return {
        'nome': conversao[:3],
        'valor': bid,
        'variacao': pct_change,
        'tendencia': tendencia
    }




if __name__ == '__main__':
    json_da_internet = buscar_cotacoes()
    
    if json_da_internet:
        print("COTAÇÕES ATUAIS")
        moedas_para_testar = ['USDBRL', 'EURBRL', 'BTCBRL']
        
        for moeda in moedas_para_testar:
            info = get_info_moeda(json_da_internet, moeda)
            
            if info:
                seta = '^' if info['tendencia'] == 'subiu' else 'v'
                
                print(f"{info['nome']}: R$ {info['valor']:.2f} {seta} ({info['variacao']:.2f}%)")