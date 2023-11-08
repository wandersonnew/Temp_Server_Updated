from decouple import config
import requests

token   = config('TOKEN_TELEGRAM')
chat_id = config('CHAT_ID')
mensagem = 'Sala dos servidores está com temperatura acima do normal.'

url = f'https://api.telegram.org/bot{token}/sendMessage'

# Parâmetros da solicitação POST
params = {
    'chat_id': chat_id,
    'text': mensagem
}

def sendMssgTelegram():
    # Envie a solicitação POST para a API do Telegram
    response = requests.post(url, data=params)

    # Verifique se a solicitação foi bem-sucedida
    if response.status_code == 200:
        print('Mensagem enviada com sucesso!')
    else:
        print(f'Falha ao enviar a mensagem. Código de status: {response.status_code}')
        print(response.text)  # Exibe a resposta da API em caso de erro
