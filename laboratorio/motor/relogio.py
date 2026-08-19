from datetime import datetime

def get_data_hora():
    agora = datetime.now()
    
    dias_semana = [
        "Segunda-feira", "Terça-feira", "Quarta-feira", 
        "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"
    ]
    
    meses = [
        "",
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    indice_semana = agora.weekday() # Retorna de 0 a 6
    indice_mes = agora.month        # Retorna de 1 a 12
    
    return {
        "hora_formatada": agora.strftime("%H:%M"),
        "segundos": agora.strftime("%S"),
        "dia": agora.day,
        "mes_texto": meses[indice_mes],
        "dia_semana": dias_semana[indice_semana],
        "ano": agora.year
    }




if __name__ == "__main__":
    tempo = get_data_hora()
    
    texto_relogio = tempo['hora_formatada']
    texto_data = f"{tempo['dia_semana']}, {tempo['dia']} de {tempo['mes_texto']} de {tempo['ano']}"
    
    print(f"Relógio Principal: {texto_relogio}")
    print(f"Data Completa: {texto_data}")