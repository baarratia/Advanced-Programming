__author__ = 'Benja'

from PyQt4 import QtGui, QtCore


class MainForm(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()

        ''' Configura geometría de la ventana'''
        self.setWindowTitle('Gato Revolution')
        self.setGeometry(200, 100, 300, 250)

        ''' Definición de acciones'''
        reiniciar = QtGui.QAction(QtGui.QIcon(None), '&Reiniciar', self)
        reiniciar.setStatusTip('Reiniciar Juego')
        reiniciar.triggered.connect(self.reiniciar)

        salir = QtGui.QAction(QtGui.QIcon(None), '&Salir', self)
        salir.setShortcut('Ctrl+Q')  # se puede agregar una combinación de teclas para ejecutar el comando
        salir.setStatusTip('Terminar la aplicación')  # muestra en la barra de estados la descripción del comando
        salir.triggered.connect(QtGui.qApp.quit)  # conecta la señal con el slot que manejará este evento

        ''' Creación de la barra de menús y de los menús'''
        menubar = self.menuBar()
        archivo_menu = menubar.addMenu('&Archivo')  # primero menú
        archivo_menu.addAction(reiniciar)
        archivo_menu.addAction(salir)

        ''' Incluye la barra de estado'''
        self.statusBar().showMessage('Turno de X')

        ''' Configura como Widget Central el formulario creado anteriormente.'''
        self.form = MiFormulario(self.statusBar())
        self.setCentralWidget(self.form)

    def reiniciar(self):
        self.form = MiFormulario(self.statusBar())
        self.setCentralWidget(self.form)


class MiFormulario(QtGui.QWidget):
    def __init__(self, status):
        super().__init__(status)
        self.init_GUI()
        self.turno = 0
        self.status = status
        self.estado = True

    def init_GUI(self):
        ''' Aquí se crea la grilla para ubicar los Widget de manera matricial'''
        grilla = QtGui.QGridLayout()
        self.setLayout(grilla)
        self.botones = {}
        valores = [' ', ' ', ' ',
                   ' ', ' ', ' ',
                   ' ', ' ', ' ']

        posicion = [(i, j) for i in range(3) for j in range(3)]
        for posicion, valor in zip(posicion, valores):
            if valor == '':
                continue
            boton = QtGui.QPushButton(valor)
            boton.resize(boton.sizeHint())
            boton.move(20, 20)
            boton.clicked.connect(self.boton_presionado)
            grilla.addWidget(boton, *posicion)
            self.botones[posicion] = boton
        self.move(150, 150)
        self.setWindowTitle('Calculator')
        self.show()

    def comprobar_juego(self):
        if self.botones[(0, 0)].text() == self.botones[(0, 1)].text() == self.botones[(0, 2)].text() != ' ':
            self.status.showMessage('Gana jugador {}'.format(self.botones[(0, 0)].text()))
            self.estado = False
        if self.botones[(1, 0)].text() == self.botones[(1, 1)].text() == self.botones[(1, 2)].text() != ' ':
            self.status.showMessage('Gana jugador {}'.format(self.botones[(1, 0)].text()))
            self.estado = False
        if self.botones[(2, 0)].text() == self.botones[(2, 1)].text() == self.botones[(2, 2)].text() != ' ':
            self.status.showMessage('Gana jugador {}'.format(self.botones[(2, 0)].text()))
            self.estado = False
        if self.botones[(0, 0)].text() == self.botones[(1, 0)].text() == self.botones[(2, 0)].text() != ' ':
            self.status.showMessage('Gana jugador {}'.format(self.botones[(0, 0)].text()))
            self.estado = False
        if self.botones[(0, 1)].text() == self.botones[(1, 1)].text() == self.botones[(2, 1)].text() != ' ':
            self.status.showMessage('Gana jugador {}'.format(self.botones[(0, 1)].text()))
            self.estado = False
        if self.botones[(0, 2)].text() == self.botones[(1, 2)].text() == self.botones[(2, 2)].text() != ' ':
            self.status.showMessage('Gana jugador {}'.format(self.botones[(0, 2)].text()))
            self.estado = False
        if self.botones[(0, 0)].text() == self.botones[(1, 1)].text() == self.botones[(2, 2)].text() != ' ':
            self.status.showMessage('Gana jugador {}'.format(self.botones[(0, 0)].text()))
            self.estado = False
        if self.botones[(0, 2)].text() == self.botones[(1, 1)].text() == self.botones[(2, 0)].text() != ' ':
            self.status.showMessage('Gana jugador {}'.format(self.botones[(0, 2)].text()))
            self.estado = False
        else:
            c = 0
            for i in self.botones:
                if self.botones[i].text() != ' ':
                    c += 1
            if c == 9:
                self.status.showMessage('Empate!')
                self.estado = False


    def boton_presionado(self):
        sender = self.sender()
        if self.estado:
            if self.turno % 2 == 0:
                movimiento = 'X'
                self.status.showMessage('Turno de O')
            else:
                movimiento = 'O'
                self.status.showMessage('Turno de X')

            if sender.text() == ' ':
                sender.setText(movimiento)
                self.turno += 1
            self.comprobar_juego()


if __name__ == '__main__':
    app = QtGui.QApplication([])

    ''' Se crea una ventana descendiente de QMainWindows'''
    form = MainForm()
    form.show()
    app.exec_()

