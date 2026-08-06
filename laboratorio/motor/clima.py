import os
import requests
from dotenv import load_dotenv


load_dotenv()
LAT = os.getenv("LATITUDE_CASA")
LON = os.getenv("LONGITUDE_CASA")
FUSO = os.getenv("FUSO_HORARIO")


url = (
    f'https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}&daily=sunset,sunrise,moon_phase,'
    f'temperature_2m_max,temperature_2m_min&current=temperature_2m,relative_humidity_2m,wind_speed_10m,'
    f'precipitation&timezone={FUSO}'
)

print(f"Buscando clima para as coordenadas: {LAT}, {LON}")


resposta = requests.get(url)
dados = resposta.json()
# print(dados)



umidade = dados['current']['relative_humidity_2m']
velocidade_vento = dados['current']['wind_speed_10m']
precipitacao = dados['current']['precipitation']

#pegar o primeiro da lista, dia atual
anoitecer = dados['daily']['sunset'][0]
amanhecer = dados['daily']['sunrise'][0]

#pega somento o horario, ignorando o dia
anoitecer_formatado = anoitecer[11:]
amanhecer_formatado = amanhecer[11:]

#temperatura
temperatura = dados['current']['temperature_2m']
temp_max_hoje = dados['daily']['temperature_2m_max'][0]
temp_min_hoje = dados['daily']['temperature_2m_min'][0]

fase_lua_api = dados['daily']['moon_phase'][0]

def mapear_fase_lua(fase):
    # Lista de tuplas (limite_superior, nome_da_fase)
    fases = [
        (0.06, "Nova"),
        (0.19, "Crescente"),
        (0.31, "Quarto Crescente"),
        (0.44, "Gibosa Crescente"),
        (0.56, "Cheia"),
        (0.69, "Gibosa Minguante"),
        (0.81, "Quarto Minguante"),
        (0.94, "Minguante")
    ]
    
    for limite, nome in fases:
        if fase < limite:
            return nome
    return "Nova"

fase_lua = mapear_fase_lua(fase_lua_api)


print(f'''-----RELATORIO-----
{temperatura}°C
{temp_min_hoje}°C - {temp_max_hoje}°C
{umidade}% umidade
{velocidade_vento}km/h
precipitação: {precipitacao}mm

{amanhecer_formatado}:::{anoitecer_formatado}

fase da lua: {fase_lua}''')