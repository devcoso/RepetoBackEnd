class RecicladoMaquina():

    def __init__(self, Oid, Maquina, Fecha,Cantidad,Monto) -> None:
        self.Oid = Oid
        self.Maquina = Maquina
        self.Fecha = Fecha
        self.Cantidad = Cantidad
        self.Monto = Monto
    
    def to_JSON(self):
        return {
            'Oid': self.Oid,
            'Maquina': self.Maquina,
            'Fecha': self.Fecha,
            'Cantidad': self.Cantidad,
            'Monto': self.Monto,
        }
    