class Operacion:

    def __init__(self, id, desc, importe, tipo, zona):
        self.id = id
        self.desc = desc
        self.importe = importe
        self.tipo = tipo
        self.zona = zona


def to_string(self):
    tipo = ['fumigacion', 'sembrado', 'cultivado', 'cosechado', 'labrado', 'arado', 'abono', 'riego', 'cuido de sembradío', 'rotacion de cultivos',
            'distribucion', 'venta', 'cultivos frutales', 'cultivos de hortalizas', 'silvicultura', 'vinicultura']
    zona = ['BA', 'CBA', 'Mza', 'Santa Fe', 'Santiago del Estero', 'La Pampa', 'TDF', 'Jujuy', 'Salta', 'Formosa', 'Misiones', 'San Luis', 'San Juan', 'La rioja'
            , 'Tucumán', 'Catamarca', 'Entre Ríos', 'Corrientes', 'Chaco', 'Santa Cruz']

    print(f'Id: {self.id}| Descripcion: {self.desc}| Importe: {self.importe}| Tipo: {tipo[self.tipo]}| Zona: {zona[self.zona]}')
