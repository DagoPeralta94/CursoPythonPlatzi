class Automovil:
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "en_reposo"
        self._motor = Motor(cilindros=4)

        print(f'Modelo: {self.modelo} - Marca: {self.marca} - Color: {self.color}')

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self.estado = 'en_movimiento'

        print(f'Estado: {self.estado} - Tipo de aceleración: {tipo}')


class Motor:
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        self._temperatura = 30
        print(f'Cantidad de inyección: {cantidad} - Cilindros: {self.cilindros} - Tipo de combustiión: {self.tipo} - Temperatura: {self._temperatura} grados')

auto = Automovil('2019', 'MAZDA', 'AZUL')
auto.acelerar('rapida')
