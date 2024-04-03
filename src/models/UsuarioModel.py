from database.db import get_connection
#Servicio de Correos
from utils.EmailSender import EmailSender
#Seguridad
from utils.Security import Security
#Usuario
from .entities.Usuario import Usuario

from decouple import config

# from utils.Security import Security
oid = "(SELECT(uuid_in(overlay(overlay(md5(random()::text || ':' || clock_timestamp()::text) placing '4' from 13) placing to_hex(floor(random()*(11-8+1) + 8)::int)::text from 17)::cstring)))"

class UsuarioModel():

    @classmethod
    def login(self,nombreUsuario,contrasenia):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                sql="""SELECT u.\"Oid\",u.\"NombreUsuario\",u.\"CambiarContrasenia\",u.\"Activo\",u.\"Eliminar\"
                                FROM  \"Usuario\" u
                                WHERE u.\"Activo\" IS TRUE 
                                AND u.\"Eliminar\" IS null
                                AND u.\"NombreUsuario\" = %s
                                AND u.\"Contrasenia\" = %s"""
                cursor.execute(sql, (nombreUsuario,contrasenia,))
                usuario = cursor.fetchone()
            connection.close()
            
            if usuario == None:
                return {
                    'status': False,
                    'mensaje': "Usuario no encontrado",
                }
            else:
                token = Security.generate_token(usuario,segundos=60*60)
                return {
                    'status': True,
                    'mensaje': "Login Exitoso",
                    'token': token
                }
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def mis_datos(self, headers):
        
        usuario = Security.verify_token(headers)
        if usuario != None:
            return {
                'status': True,
                'mensaje': "Usuario autorizado",
                'Usuario': usuario
            }
        else:
            return {
                'status': False,
                'mensaje': 'Usuario no autorizado'
            }
   
    @classmethod
    def update_usuario_contrasenia(self,header,contrasenia):
        if(len(contrasenia) < 8 or len(contrasenia) > 16):
            return {
                'status': False,
                'mensaje': 'Contraseña inválido'
            }
        try:
            usuario = Security.verify_token(header)
            if usuario!=None:
                connection = get_connection()
                with connection.cursor() as cursor:
                    sql="""UPDATE \"Usuario\" 
                        SET \"Contrasenia\"=%s,
                        \"CambiarContrasenia\" = false 
                        WHERE \"Oid\"=%s"""
                    cursor.execute(sql, (contrasenia, usuario['Oid'],))
                    connection.commit()
                connection.close()
                return {
                    'status': True,
                    'mensaje': 'Actualizado de Contraseña Correcto'
                }
            else:
                 return {
                    'status': False,
                    'mensaje': 'Tiempo finalizado'
                }

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_usuario_restablecer(self,correo):
        if Usuario.is_valid_email(correo)==False:
            return {
                    'status':   False,
                    'mensaje': 'Correo invalido'
                }
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql="""SELECT "Oid",'Correo' FROM "Persona" WHERE "Correo"=%s"""
                cursor.execute(sql, (correo,))
                usuario=cursor.fetchone()
            connection.close()
            if usuario != None:
                token = Security.generate_token(authenticated_user=usuario,segundos=60*5)

                connection = get_connection()
                with connection.cursor() as cursor:
                    sql="""UPDATE \"Usuario\" 
                            SET \"CambiarContrasenia\" = true 
                            WHERE \"Oid\"=%s"""
                    cursor.execute(sql, (usuario[0],))
                    connection.commit()
                connection.close()

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
                            <p>Da click en este <a href="{config('FRONTEND_URL')}auth/reset-password/{token}">enlace</a> para reestablecer tu contraseña. Si tú no quieres reestabelecer tu contraseña, entonces ignora este email.</p>
                        </body>
                    </html>"""
                exitosoEnvio = EmailSender.envio_correo("Repeto",correo,html_content,"Restablecer Contraseña")
                if exitosoEnvio == True:
                    return {
                        'status':   True,
                        'mensaje': 'Se ha enviado un correo'
                    }
                else:
                    return {
                        'status':   False,
                        'mensaje': 'No se pudo enviar correo'
                    }
            else:
                return {
                    'status': False,
                    'mensaje': 'El Usuario no está registrado'
                }
        except Exception as ex:
            raise Exception(ex)
         
    @classmethod
    def get_usuario(self,Oid):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                sql="""SELECT u.\"Oid\",u.\"NombreUsuario\",u.\"CambiarContrasenia\",u.\"Activo\",u.\"Eliminar\" ,
                                p.\"Nombre\",p.\"PrimerApellido\",p.\"SegundoApellido\",p.\"Correo\",p.\"Telefono\",p.\"FechaRegistro\"
                                FROM \"Persona\" p 
                                INNER JOIN \"Usuario\" u ON u.\"Oid\" = p.\"Oid\" 
                                WHERE u.\"Activo\" IS TRUE 
                                AND u.\"Eliminar\" IS null
                                AND P.\"Oid\" = '%s'"""
                cursor.execute(sql, (Oid))
                usuario = cursor.fetchone()
            connection.close()

            return usuario
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_usuario(self,usuario):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql_buscar="""SELECT \"Oid\" FROM \"Usuario\" 
                                WHERE \"NombreUsuario\"=%s"""
                cursor.execute(sql_buscar, (usuario.NombreUsuario,))
                user=cursor.fetchone()
            connection.close()
            if user == None:
                connection = get_connection()
                with connection.cursor() as cursor:
                    sql="""INSERT INTO \"Usuario\" (\"Oid\",\"NombreUsuario\",\"Contrasenia\",\"CambiarContrasenia\",\"Activo\") 
                        VALUES ((SELECT(uuid_in(overlay(overlay(md5(random()::text || ':' || clock_timestamp()::text) placing '4' from 13) placing to_hex(floor(random()*(11-8+1) + 8)::int)::text from 17)::cstring))),
                          %s, %s, FALSE,TRUE) RETURNING \"Oid\",\"NombreUsuario\""""
                    cursor.execute(sql, (usuario.NombreUsuario, usuario.Contrasenia,))
                    connection.commit()

                    affected_rows = cursor.rowcount
                    nuevo_usuario = cursor.fetchone()
                    sql_persona="""INSERT INTO \"Persona\" (\"Oid\",\"Nombre\",\"PrimerApellido\",\"SegundoApellido\",\"Correo\",\"FechaRegistro\") 
                        VALUES (%s,%s, %s,%s,%s,(SELECT NOW())) RETURNING \"Oid\""""
                    cursor.execute(sql_persona, (nuevo_usuario[0],usuario.Nombre, usuario.PrimerApellido,usuario.SegundoApellido,usuario.Correo,))
                    connection.commit()

                    connection.close()
                    
                    if affected_rows == 1:
                        return {
                            'status': True,
                            'mensaje': "Nuevo Usuario",
                        }
                    else:
                        return {
                            'status': False,
                            'mensaje': "Error Usuario"
                        }
            else:
                return {
                    'status': False,
                    'mensaje': "Nombre de Usuario ya registrado"
                }
        except Exception as ex:
            return {
                'status': False,
                'mensaje': Exception(ex)
            }

    @classmethod
    def get_usuarios(self):
        try:
            connection = get_connection()
            usuarios = []

            with connection.cursor() as cursor:
                sql="SELECT  \"Oid\",\"NombreUsuario\",\"CambiarContrasenia\",\"Activo\",\"Eliminar\" FROM \"Usuario\" ORDER BY \"NombreUsuario\"  ASC"
                cursor.execute(sql)
                resultset = cursor.fetchall()

                for row in resultset:
                    usuario = Usuario(Oid=row[0], NombreUsuario=row[1], CambiarContrasenia=row[2],Activo=row[3], Eliminar=row[4])
                    usuarios.append(usuario.to_JSON())

            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)
        
