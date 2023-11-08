from smtplib import SMTP

def sendEmail():
    try:
        servidor_email = SMTP('smtp.gmail.com', 587)
        servidor_email.starttls()
        servidor_email.login('wanderson.stacasa@gmail.com', 'mlmp kcgf shru fzjx ')
        
        remetente = 'wanderson.stacasa@gmail.com'
        destinatarios = ['wanderson.stacasa@gmail.com', 'alessandrosilvastacasa@gmail.com', 'jason@stacasa.com.br', 'davynadionisio2@gmail.com']
        conteudo = 'Servidor com temperatura acima de 18°C.'
        
        servidor_email.sendmail(remetente, destinatarios, conteudo.encode())
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    finally:
        servidor_email.quit()