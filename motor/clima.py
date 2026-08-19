import requests
import os
from dotenv import load_dotenv


def mapear_fase_lua(fase):
    # limite_superior, nome_da_fase
    fases = [
        (0.06, 'Nova'),
        (0.19, 'Crescente'),
        (0.31, 'Quarto Crescente'),
        (0.44, 'Gibosa Crescente'),
        (0.56, 'Cheia'),
        (0.69, 'Gibosa Minguante'),
        (0.81, 'Quarto Minguante'),
        (0.94, 'Minguante')
    ]
    
    for limite, nome in fases:
        if fase < limite:
            return nome
    return 'Nova'



def buscar_dados_brutos():
    load_dotenv()
    LAT = os.getenv('LATITUDE_CASA')
    LON = os.getenv('LONGITUDE_CASA')
    FUSO = os.getenv('FUSO_HORARIO')

    if not LAT or not LON or not FUSO:
        print("ERRO CRÍTICO: Variáveis de clima não encontradas no arquivo .env")
        return None

    url = (
        f'https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&daily=sunset,sunrise,moon_phase,'
        f'temperature_2m_max,temperature_2m_min&current=temperature_2m,relative_humidity_2m,wind_speed_10m,'
        f'precipitation&timezone={FUSO}'
    )

    resp = requests.get(url)

    if resp.status_code == 200:
        return resp.json()
    else:
        print(f"Erro na Internet: A API respondeu com o código {resp.status_code}")
        return None



def get_clima_atual(dados):
    if not dados:
        return None
    
    return {
        'temperatura': dados['current']['temperature_2m'],
        'umidade': dados['current']['relative_humidity_2m'],
        'velocidade_vento': dados['current']['wind_speed_10m'],
        'precipitacao': dados['current']['precipitation']
    }



def get_extremos_dia(dados):
    if not dados:
        return None
    
    return {
        'temp_max': dados['daily']['temperature_2m_max'][0],
        'temp_min': dados['daily']['temperature_2m_min'][0]
    }



def get_astronomia(dados):
    if not dados:
        return None
    
    anoitecer = dados['daily']['sunset'][0]
    amanhecer = dados['daily']['sunrise'][0]
    fase_lua_api = dados['daily']['moon_phase'][0]

    return {
        'amanhecer': amanhecer[11:],
        'anoitecer': anoitecer[11:],
        'fase_lua': mapear_fase_lua(fase_lua_api) # Chama a função utilitária aqui!
    }




if __name__ == '__main__':
    json_da_internet = buscar_dados_brutos()
    
    if json_da_internet:
        print("CLIMA ATUAL")
        print(get_clima_atual(json_da_internet))
        
        print("\nEXTREMOS DO DIA")
        print(get_extremos_dia(json_da_internet))
        
        print("\nASTRONOMIA")
        print(get_astronomia(json_da_internet))