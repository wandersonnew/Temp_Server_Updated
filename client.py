import socket
import pickle5 as pickle
from send_email import sendEmail
from telegram import sendMssgTelegram

host = '0.0.0.0'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:
    dados = pickle.loads(client_socket.recv(1024))
    print(f"Recebido: {dados}")

    if dados[1] != 'Falha no Sensor':
        temp = float(dados[1].replace('C', '').replace(',', '.').strip())
        if temp > 28:
            sendEmail()
            sendMssgTelegram()