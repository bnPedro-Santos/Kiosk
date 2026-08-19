import requests
from datetime import datetime

def buscar_feriados_do_ano():
    ano = datetime.today().year
    url = f'https://brasilapi.com.br/api/feriados/v1/{ano}'
    
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



def get_proximo_feriado(dados):
    # Se os dados vieram vazios, aborta
    if not dados:
        return None
        
    hoje = datetime.today().date()
    
    for feriado in dados:
        data_texto = feriado['date']
        nome_feriado = feriado['name']
        
        data_real = datetime.strptime(data_texto, '%Y-%m-%d').date()
        
        if data_real >= hoje:
            dias_restantes = (data_real - hoje).days
            
            return {
                'nome': nome_feriado,
                'data_original': data_texto,
                'dias_restantes': dias_restantes
            }
            
    return None




if __name__ == '__main__':
    json_da_internet = buscar_feriados_do_ano()
    
    if json_da_internet:
        proximo = get_proximo_feriado(json_da_internet)
        
        if proximo:
            print("PRÓXIMO FERIADO")
            print(f"Evento: {proximo['nome']}")
            print(f"Data: {proximo['data_original']}")
            
            if proximo['dias_restantes'] == 0:
                print("É HOJE!")
            elif proximo['dias_restantes'] == 1:
                print("Falta: 1 dia")
            else:
                print(f"Faltam: {proximo['dias_restantes']} dias")
        else:
            print("Não há mais feriados nacionais neste ano.")