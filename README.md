# ServidorTemperatura

Aplicação em Python usada para verificar a temperatura da sala de servidores.

Quando a temperatura atinge temperatura acima de 28 graus, emite envio de emails para os integrantes do
setor de Tecnologia da Informação para alertar que há problema na sala de servidores e envia mensagens para o grupo no telegram.

## Python e Bibliotecas

Python             3.10.12

beautifulsoup4     4.12.2

pickle5            0.0.11

secure-smtplib     0.1.1

requests           2.31.0

secure-smtplib     0.1.1


## Tutorial de configurações

#### Cria virtualenv

Precisa ter o virtualenv instalado.

Rodar o seguinte comando para criar a virtualenv:

```
$ python3 -m venv env
```

#### Instalar as bibliotecas

Para instalar as dependências na virtualenv deve ativá-la, estando no mesmo diretório:

```
$ source env/bin/activate
```
e instalar as bibliotecas:

```
$ pip install pickle5
$ pip install secure-smtplib
$ pip install python-decouple
$ pip install beautifulsoup4
$ pip install requests
```




