import psutil

def get_uso_cpu():
    try:
        # Retorna apenas o número puro (float)
        return psutil.cpu_percent(interval=1)
    except Exception as erro:
        print(f"Erro Crítico ao ler CPU: {erro}")
        return None

def get_uso_memoria():
    try:
        mem = psutil.virtual_memory()
        
        return {
            'total_gb': mem.total / (1024**3),
            'disponivel_gb': mem.available / (1024**3),
            'percentual_uso': mem.percent
        }
    except Exception as erro:
        print(f"Erro Crítico ao ler Memória: {erro}")
        return None




if __name__ == '__main__':
    cpu = get_uso_cpu()
    
    if cpu is not None:
        print("💻 --- MONITORAMENTO DE CPU ---")
        print(f"Uso atual: {cpu}%")
        
    print("\n")
    
    memoria = get_uso_memoria()
    
    if memoria is not None:
        print("🧠 --- MONITORAMENTO DE MEMÓRIA ---")
        print(f"Memória Total: {memoria['total_gb']:.2f} GB")
        print(f"Memória Disponível: {memoria['disponivel_gb']:.2f} GB")
        print(f"Uso de Memória: {memoria['percentual_uso']}%")