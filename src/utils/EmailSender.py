import smtplib
from email.message import EmailMessage
from decouple import config

class EmailSender:
    @classmethod
    def send_recovery_email(self, email, token):
        # Crear un objeto EmailMessage
        msg = EmailMessage()

        # Configurar los campos del mensaje
        msg['Subject'] = 'Recupera tu cuenta'
        msg['From'] = 'repeto@repeto.com'
        msg['To'] = email

        # Contenido HTML del mensaje
        html_content = f"""
            <html>
                <head>
                            <title>Recupera tu cuenta de Repeto</title>
                            <style>
                                * {{
                                    font-family: Arial, sans-serif;
                                    color: #1e293b;
                                }}
                                body {{
                                    margin: 0;
                                    padding: 50px;
                                }}
                                h1 {{
                                    text-align: center;
                                    font-size: 20px;
                                }}
                                span {{
                                    color: #65a30d;
                                }}
                                p {{
                                    font-size: 16px;
                                }}
                                a {{
                                    text-decoration: none;
                                    color: #65a30d;
                                    font-weight: bold;
                                }}
                            </style>
                        </head>
                        <body>
                            <h1 >Recupera tu cuenta de <span>Repeto</span></h1>
                            <p>Da click en este <a href="{config('FRONTEND_URL')}/reset-password/{token}">enlace</a> para reestablecer tu contraseña. Si tú no quieres reestabelecer tu contraseña, entonces ignora este email.</p>
                        </body>
            </html>"""

        # Agregar contenido HTML al mensaje
        msg.add_alternative(html_content, subtype='html')

        with smtplib.SMTP(config('EMAIL_HOST'), config('EMAIL_PORT') ) as server:
            server.login(config('EMAIL_USER'), config('EMAIL_PASS'))
            server.send_message(msg)
        print("Email sent \n\n ----------------- \n\n")
