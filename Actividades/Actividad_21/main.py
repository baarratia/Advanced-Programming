#!/usr/bin/env python
#-*- coding:utf-8 -*-

from PyQt4 import QtCore, QtGui
import datetime
import pickle
import os


class Cliente:
    def __init__(self, nombre, id, dinero):
        self.nombre = nombre
        self.id = id
        self.dinero_gastado = dinero
        self.fecha_U_compra = 0

    def __setstate__(self, state):
        fecha = str(datetime.now())
        state.update({"fecha_U_compra" : fecha})
        self.__dict__ = state


class VentanaCajero(QtGui.QDialog):

    def __init__(self, parent=None, username=""):
        super(VentanaCajero, self).__init__(parent)

        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)

        self.clienteLabel = QtGui.QLabel("Nombre cliente", self)
        self.clienteText = QtGui.QLineEdit(self)
        self.idLabel = QtGui.QLabel("RUT", self)
        self.idText = QtGui.QLineEdit(self)
        self.gastadoLabel = QtGui.QLabel("Gastado", self)
        self.gastadoText = QtGui.QLineEdit(self)

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.clienteLabel)
        self.verticalLayout.addWidget(self.clienteText)
        self.verticalLayout.addWidget(self.idLabel)
        self.verticalLayout.addWidget(self.idText)
        self.verticalLayout.addWidget(self.gastadoLabel)
        self.verticalLayout.addWidget(self.gastadoText)
        self.verticalLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.serializarCliente)
        self.buttonBox.rejected.connect(self.close)

    def serializarCliente(self):

        nombre_archivo = self.idText.text() + 'walkcart'
        cliente = Cliente(self.clienteText.text(), self.idText.text())
        if os.path.isfile("/ClientesDB/{}".format(nombre_archivo)):
            with open(nombre_archivo, 'rb') as file:
                pickle.load(file)
        else:
            with open(nombre_archivo, 'wb') as file:
                pickle.dump(cliente, file)

        self.clienteText.setText("")
        self.idText.setText("")
        self.gastadoText.setText("")


class VentanaAdmin(QtGui.QDialog):

    def __init__(self, parent=None):
        super(VentanaAdmin, self).__init__(parent)

        self.archivoButton = QtGui.QPushButton("TOP-LIST")
        self.archivoButton.clicked.connect(self.generarArchivo)

        self.cancelButton = QtGui.QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.close)

        self.horizontalLayout = QtGui.QVBoxLayout(self)
        self.horizontalLayout.addWidget(self.archivoButton)
        self.horizontalLayout.addWidget(self.cancelButton)

    def generarArchivo(self):
        pass


class Input(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Input, self).__init__(parent)

        self.userNameText = QtGui.QLineEdit(self)

        self.pushButtonWindow = QtGui.QPushButton(self)
        self.pushButtonWindow.setText("Iniciar Sesión")
        self.pushButtonWindow.clicked.connect(self.on_pushButton_clicked)

        self.layout = QtGui.QHBoxLayout(self)
        self.layout.addWidget(self.userNameText)
        self.layout.addWidget(self.pushButtonWindow)

    @QtCore.pyqtSlot()
    def on_pushButton_clicked(self):
        with open('cajeros.walkcart', 'rb') as file:
                lista = pickle.load(file)
        x = False
        for i in lista:
            if i == self.userNameText.text():
                self.ventana = VentanaCajero()
                self.ventana.show()
                self.hide()
                x = True
        if not x:
            self.userNameText.setText('Error')




if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Log-in WM')

    main = Input()
    main.show()

    sys.exit(app.exec_())
