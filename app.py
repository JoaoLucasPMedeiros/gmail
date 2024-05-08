import os
#DotEnv -  pip install python-dotenv
from dotenv import load_dotenv
import pathlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import smtplib


load_dotenv()


CAMINHO_HTML = pathlib.Path(__file__).parent/'index.html'
#DADOS DO REMETENTE e destinatario

remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente 

#Config - SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smpt_username = os.getenv('FROM_EMAIL', '')
smpt_password = os.getenv('EMAIL', 'EMAIL_PASSWORD')

#MSG de text
with open(CAMINHO_HTML, 'r') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Usuario')

#Transformar nossa mensagem em MUMEMultiparts
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Está é um email teste com python'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Envia o email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smpt_username, smpt_password)
    server.send_message(mime_multipart)
    print("Email enviado")