from werkzeug.security import generate_password_hash, check_password_hash

class User () :
    def __init__(self, oid, usuario_nombre, contrasenia, cambiar_contrasenia=False, activo=True):
        self.oid = id
        self.usuario_nombre = usuario_nombre
        self.contrasenia = contrasenia
        self.cambiar_contrasenia = cambiar_contrasenia
        self.activo = activo
        