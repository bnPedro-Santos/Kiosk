import psutil

#cpu_percent permite obter o uso da CPU (intervalo de 1sec)
print(f'CPU: {psutil.cpu_percent(interval=1)}%')
print('\n')

#virtual_memory permite obter o uso da memoria (bytes, por isso o 1024**3, para converter para GB)
mem = psutil.virtual_memory()
print(f'Memória total: {mem.total / (1024**3):.2f} GB')
print(f'Memória disponível: {mem.available / (1024**3):.2f} GB')
print(f'Uso de memória: {mem.percent}%')
print('\n')

#net_io_counters permite obter o tráfego de rede
# net = psutil.net_io_counters()
# print(f'Bytes enviados: {net.bytes_sent}')
# print(f'Bytes recebidos: {net.bytes_recv}')

