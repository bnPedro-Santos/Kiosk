import requests
import os
from dotenv import load_dotenv

def buscar_metas_gist():
    load_dotenv()
    url = os.getenv('URL_RAW_METAS')

    if not url:
        print("ERRO CRÍTICO: O Python NÃO achou a variável 'URL_RAW_METAS'.")
        print("Motivos: O link não está no arquivo .env ou a pasta está errada.")
        return None

    try:
        resp = requests.get(url)
        
        if resp.status_code == 200:
            return resp.text
        else:
            print(f"Erro na Internet: O GitHub respondeu com o código {resp.status_code}")
            return None
            
    except requests.exceptions.RequestException as erro:
        print(f"Erro Crítico de Conexão: Falha ao acessar o GitHub. ({erro})")
        return None




if __name__ == '__main__':
    texto_das_metas = buscar_metas_gist()
    
    if texto_das_metas:
        print("METAS DO MOMENTO")
        print(texto_das_metas)