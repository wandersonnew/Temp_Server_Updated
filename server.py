import socket
import time
import pickle5 as pickle
import requests
from temp_server import getTemp

host = '0.0.0.0'  # Ou '127.0.0.1' para conexões locais
port = 12345

# url do site que se deseja fazer scraping
url = 'http://10.10.10.201:8080/index.html'

# pegar o agente do browser (forma genérica)
agent = requests.get('https://www.google.com/')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

print(f"Servidor ativo em {host}:{port}")

client_socket, client_address = server_socket.accept()
print(f"Conexão recebida de {client_address}")

while True:
    mensagem = pickle.dumps(getTemp(url, agent))
    client_socket.send(mensagem)
    time.sleep(29)

# Feche a conexão com o cliente
client_socket.close()