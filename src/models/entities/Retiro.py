class Reciclado():

    def __init__(self, Oid,Persona, Fecha, Monto) -> None:
        self.Oid = Oid
        self.Persona = Persona
        self.Fecha = Fecha
        self.Monto = Monto
    
    def to_JSON(self):
        return {
            'Oid': self.Oid,
            'Persona': self.Persona,
            'Fecha': self.Fecha,
            'Monto': self.Monto,
        }
    