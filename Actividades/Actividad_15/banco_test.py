import unittest
from banco import Banco, CajeroAutomatico, Usuario


class TestCajeros(unittest.TestCase):

    def setUp(self):
        self.Banco = Banco('Seguritas')
        self.cajero = CajeroAutomatico(self.Banco)
        self.Banco.agregar_usuario('123456', 'Pedro', '1234')
        self.Banco.usuarios[0].saldo = 1000
        self.Banco.agregar_usuario('123457', 'Juan', '3412')
        self.Banco.agregar_usuario('123458', 'Martin', '2143')

        #self.ruts = [123456, 234156, 123451, 123457, 123458, 9012345]
        #self.claves = [1234, 234156, 3412, 123457, 2143, 9012345]

    def test_credenciales(self):
        self.assertTrue(self.Banco.verificar_login('123458', '2143'))
        self.assertFalse(self.Banco.verificar_login('123458', '12345'))
        self.assertIsNone(self.Banco.verificar_login('90', '12345'))

    def test_dd(self): #dinero disponible
        self.assertIsNone(self.cajero.retirar_dinero('123456', '1234', 1000))

    def test_actualizado(self):
        saldo_inicial = self.Banco.usuarios[0].saldo
        self.cajero.retirar_dinero('123456', '1234', 1000)
        self.assertTrue(self.Banco.usuarios[0].saldo != saldo_inicial)

    def test_comprobar_cuenta(self):
        self.assertTrue(self.Banco.buscar_tercero('123458'))
        self.assertFalse(self.Banco.buscar_tercero('90'))

    def test_actualizacion_tras_transferencia(self):
        saldo_inicial = self.Banco.usuarios[0].saldo
        self.cajero.transferir_dinero('123456', '1234', '123457', 1000)
        self.assertTrue(self.Banco.usuarios[0].saldo != saldo_inicial and self.Banco.usuarios[1].saldo != 0)

    def test_errores_transferencia(self):
        self.cajero.transferir_dinero('123456', '1234', '123457', 1000)


if __name__ == "__main__":
    unittest.main()
