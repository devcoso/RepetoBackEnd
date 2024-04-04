class Reciclado():

    def __init__(self, Oid,Persona, Maquina, Fecha, Cantidad, Monto) -> None:
        self.Oid = Oid
        self.Persona = Persona
        self.Maquina = Maquina
        self.Fecha = Fecha
        self.Cantidad = Cantidad
        self.Monto = Monto
    
    def to_JSON(self):
        return {
            'Oid': self.Oid,
            'Persona': self.Persona,
            'Maquina': self.Maquina,
            'Fecha': self.Fecha,
            'Cantidad': self.Cantidad,
            'Monto': self.Monto,
        }
    