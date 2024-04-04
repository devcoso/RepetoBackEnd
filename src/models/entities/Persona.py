class Persona():

    def __init__(self, Oid,Nombre,PrimerApellido,SegundoApellido,Correo,Telefono,Ciudad,FechaRegistro,Observaciones,TotalReciclado,TotalRetirado,TotalDisponible) -> None:
        self.Oid = Oid
        self.Nombre = Nombre
        self.PrimerApellido = PrimerApellido
        self.SegundoApellido = SegundoApellido
        self.Correo = Correo
        self.Telefono = Telefono
        self.Ciudad = Ciudad
        self.FechaRegistro = FechaRegistro
        self.Observaciones = Observaciones
        self.TotalReciclado = TotalReciclado
        self.TotalRetirado = TotalRetirado
        self.TotalDisponible = TotalDisponible
    
    def to_JSON(self):
        return {
            'Oid': self.Oid,
            'Nombre': self.Nombre,
            'PrimerApellido': self.PrimerApellido,
            'SegundoApellido': self.SegundoApellido,
            'Correo': self.Correo,
            'Telefono': self.Telefono,
            'Ciudad': self.Ciudad,
            'FechaRegistro': self.FechaRegistro,
            'Observaciones': self.Observaciones,
            'TotalReciclado': self.TotalReciclado,
            'TotalRetirado': self.TotalRetirado,
            'TotalDisponible': self.TotalDisponible,
        }
    