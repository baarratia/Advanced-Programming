import pytest
import string
import encriptador
import os


# Para verificar que la funcion es biyectiva puedes usar:
def check_bijection(rot):
    dom = range(26)
    rec = []

    for x in dom:
        y = rot.get(x)
        assert y is not None
        rec.append(y)

    assert set(dom) == set(rec)


def check_simetric(rot):
    dom = 26

    for x in range(dom):
        y = rot.get(x)
        if y is not None:
            z = rot.get(y)
            assert x == z


def setup_module(module):
    encriptador.create_alphabet(list(string.ascii_lowercase))


class TestRotor:

    def setup_class(cls):
        cls.rotors = []
        for i in range(1, 4):
            cls.rotors.append(
                encriptador.Rotor('files\\rotor{0}.txt'.format(i))
            )

    def test_function(self):
        check_bijection(self.rotors)
        # Puedes usar a los rotores llamando: self.rotors


class TestReflector:

    def setup_class(cls):
        cls.reflector = encriptador.Reflector('files\\reflector.txt')

    def test_function(self):
        # Puedes usar al reflector llamando: self.reflector
        check_bijection(self.reflector)
        check_simetric(self.reflector)


class TestEncoder:

    def setup_class(cls):
        rots = ['files\\rotor1.txt', 'files\\rotor2.txt', 'files\\rotor3.txt']
        refl = 'files\\reflector.txt'
        cls.enc = encriptador.Encoder(rots, refl)
        cls.listabuena = ['thequickbrownfoxjumpsoverthelazydog', 'python', 'bang', 'libelula', 'csharp']
        cls.listamala = ['ñandu', 'canción']

    def test_encoding(self):
        for i in self.listabuena:
            a = self.enc.encrypt(i)
            b = self.enc.encrypt(a)

    def test_exception(self):
        for i in self.listamala:
            a = self.enc.encrypt(i)
            b = self.enc.encrypt(a)

