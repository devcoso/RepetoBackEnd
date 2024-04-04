class Maquina():

    def __init__(self, Oid,Nombre, Latitud, Longitud, Ciudad, Activo,Eliminar) -> None:
        self.Oid = Oid
        self.Nombre = Nombre
        self.Latitud = Latitud
        self.Longitud = Longitud
        self.Ciudad = Ciudad
        self.Activo = Activo
        self.Eliminar = Eliminar
    
    def to_JSON(self):
        return {
            'Oid': self.Oid,
            'Nombre': self.Nombre,
            'Latitud': self.Latitud,
            'Longitud': self.Longitud,
            'Ciudad': self.Ciudad,
            'Activo': self.Activo,
            'Eliminar': self.Eliminar,
        }
    