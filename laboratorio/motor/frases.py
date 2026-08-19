import json
import random
import os


def get_frase_aleatoria():
    # JSON feito por Ricardo Fiorini
    caminho_arquivo = r'laboratorio\motor\frases\frases.json'
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            lista_de_frases = json.load(arquivo)
            
        if not lista_de_frases:
            return None
            
        escolha = random.choice(lista_de_frases)
        
        return {
            'texto': escolha.get('text', 'Frase não encontrada'),
            'autor': escolha.get('author', 'Autor desconhecido')
        }
        
    except FileNotFoundError:
        print(f"Erro Crítico: O arquivo de frases não foi encontrado em '{caminho_arquivo}'")
        return None
    except json.JSONDecodeError:
        print("Erro Crítico: O arquivo frases.json está corrompido (não é um JSON válido).")
        return None
    except Exception as erro:
        print(f"Erro inesperado no motor de frases: {erro}")
        return None


if __name__ == '__main__':
    frase_zen = get_frase_aleatoria()
    
    if frase_zen:
        print("FRASE ZEN DO DIA")
        print(f"\"{frase_zen['texto']}\"")
        print(f"- {frase_zen['autor']}")