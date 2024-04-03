import re

class Usuario():

    def __init__(self, Oid,NombreUsuario,Contrasenia,CambiarContrasenia,Activo,Eliminar,
                 Nombre,PrimerApellido,SegundoApellido,Correo,Telefono,Observaciones,Ciudad,FechaRegistro) -> None:
        self.Oid = Oid
        self.NombreUsuario = NombreUsuario
        self.Contrasenia = Contrasenia
        self.CambiarContrasenia = CambiarContrasenia
        self.Activo = Activo
        self.Eliminar = Eliminar
        self.Nombre = Nombre
        self.PrimerApellido = PrimerApellido
        self.SegundoApellido = SegundoApellido
        self.Correo = Correo
        self.Telefono = Telefono
        self.Observaciones = Observaciones
        self.Ciudad = Ciudad
        self.FechaRegistro = FechaRegistro
    
    def to_JSON(self):
        return {
            'Oid': self.Oid,
            'NombreUsuario': self.NombreUsuario,
            'Contrasenia': self.Contrasenia,
            'CambiarContrasenia': self.CambiarContrasenia,
            'Activo': self.Activo,
            'Eliminar': self.Eliminar,
            'Nombre': self.Nombre,
            'PrimerApellido': self.PrimerApellido,
            'SegundoApellido': self.SegundoApellido,
            'Correo': self.Correo,
            'Telefono': self.Telefono,
            'Observaciones': self.Observaciones,
            'Ciudad': self.Ciudad,
            'FechaRegistro': self.FechaRegistro,
        }
    
    def is_valid_email(email):
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        return bool(re.match(regex, email))