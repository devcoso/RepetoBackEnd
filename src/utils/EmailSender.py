import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from decouple import config

class EmailSender:
    @classmethod
    def envio_correo(self, emisor,receptor,cuerpo,titulo):
       # Create a MIME multipart message
        msg = MIMEMultipart('alternative')

        # Cabecera de Correo
        msg['Subject'] = titulo
        msg['From'] = emisor
        msg['To'] = receptor
        html_content = MIMEText(cuerpo, _subtype='html')
        msg.attach(html_content)

        try:
            email_host = config('EMAIL_HOST')
            email_port = config('EMAIL_PORT')
            email_user = config('EMAIL_USER')
            email_pass = config('EMAIL_PASS')
        except (KeyError, AttributeError) as e:
            return False

        # Envio de correo por medio de smtplib
        try:
            with smtplib.SMTP(email_host, email_port) as server:
                server.starttls()
                server.login(email_user, email_pass)
                server.sendmail(emisor, receptor, msg.as_string())
            return True
        except smtplib.SMTPException as e:
            return False
            