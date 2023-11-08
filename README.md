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

#### Criar os serviços

Criar os serviços no diretório: /etc/systemd/system

Em User, colocar o usuário do sistema operacional.
Em WorkingDirectory, colocar o caminho do projeto.
Em ExecStart, o caminho do projeto e o arquivo bash que inicia o serviço.

Serviço servidor:

Para criar o arquivo:

```
$ sudo nano servidor.service
```

colar o código abaixo alterando de acordo com as especificaçẽs acima:

```
[Unit]
Description=Servidor de Temperatura

[Service]
Type=simple
User=wanderson
WorkingDirectory=/home/wanderson/Documentos/serv_temp/
ExecStart=/home/wanderson/Documentos/serv_temp/run_server_temp.sh

[Install]
WantedBy=multi-user.target
```

para finalizar, CTRL + O para salvar e CTRL + X para sair.

Repetir configurações para o serviço cliente:

```
$ sudo nano cliente.service
```

```
[Unit]
Description=Servidor de Temperatura

[Service]
Type=simple
User=wanderson
WorkingDirectory=/home/wanderson/Documentos/serv_temp/
ExecStart=/home/wanderson/Documentos/serv_temp/run_client_temp.sh

[Install]
WantedBy=multi-user.target
```

##### Rodando os serviços

Para rodar os serviços executar os comandos:

```
$ sudo systemctl daemon-reload
```

```
$ sudo systemctl start servidor.service
$ sudo systemctl start servidor.service
$ sudo systemctl enable servidor.service
$ sudo systemctl status servidor.service
```

se o status estiver ativo, está funcionando.

** OBS: ** Iniciar sempre o servidor primeiro (servidor.service).

Repetir para cliente.service.

## Contatos:

---

<img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/40368246?s=400&u=a7402c2d5af1e41852d39eaf80cb2154223f80db&v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Wanderson Duarte Alves</b></sub>

Bacharelado em Ciências da Computação, programador e fascinado por Linux.

Contato!

[![Gmail Badge](https://img.shields.io/badge/-wandersondrtlvs.new@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:wandersondrtlvs.new@gmail.com)](mailto:wandersondrtlvs.new@gmail.com)



