__author__ = 'JPSCHELE'

from PyQt4 import QtGui, uic
from PyQt4 import QtCore, QtGui
import random

'''la division de los numeros es entera, no se utilizan decimales en la respuesta'''
formulario = uic.loadUiType("cccc.ui")
print(formulario[0], formulario[1])

class MainWindow(formulario[0], formulario[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # se inicializa la interfaz creada en Qt Designer

        self.pushButton_1.clicked.connect(self.conseguir_operacion)
        self.pushButton_2.clicked.connect(self.comprobar)


    def conseguir_operacion(self):
        for rb_id in range(1,5):
            if getattr(self, 'radioButton' + str(rb_id)).isChecked():
                opcion = getattr(self, 'radioButton' + str(rb_id)).text()
                if opcion == 'SUMA':
                    self.label_op.setText('+')
                    self.a,self.b = self.asignar()
                    self.label_d1.setText(str(self.a))
                    self.label_d2.setText(str(self.b))
                elif opcion == 'RESTA':
                    self.label_op.setText('-')
                    self.a,self.b = self.asignar()
                    self.label_d1.setText(str(self.a))
                    self.label_d2.setText(str(self.b))
                elif opcion == 'MULTIPLICACION':
                    self.label_op.setText('*')
                    self.a,self.b = self.asignar()
                    self.label_d1.setText(str(self.a))
                    self.label_d2.setText(str(self.b))
                elif opcion == 'DIVISION':
                    self.label_op.setText('/')
                    self.a,self.b = self.asignar()
                    self.label_d1.setText(str(self.a))
                    self.label_d2.setText(str(self.b))

    def comprobar(self):
        for rb_id in range(1,5):
            if getattr(self, 'radioButton' + str(rb_id)).isChecked():
                opcion = getattr(self, 'radioButton' + str(rb_id)).text()
                if opcion == 'SUMA':
                    self.Mensaje(self.SUMA(self.a,self.b,int(self.lineEdit_resultado.text())))
                elif opcion == 'RESTA':
                    self.Mensaje(self.RESTA(self.a,self.b,int(self.lineEdit_resultado.text())))
                elif opcion == 'MULTIPLICACION':
                    self.Mensaje(self.MULTIPLICACION(self.a,self.b,int(self.lineEdit_resultado.text())))
                elif opcion == 'DIVISION':
                    self.Mensaje(self.DIVISION(self.a,self.b,int(self.lineEdit_resultado.text())))







    def Mensaje(self, texto):
        msgBox = QtGui.QMessageBox()
        msgBox.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        msgBox.setText(texto)
        ret = msgBox.exec_()


    def asignar(self):
        a = random.randrange(1, 20)
        if a != 1:
            b = random.randrange(1, a)
        else:
            b = 1
        return a,b


    def SUMA(self, a,b, resultado):
        if a+b != resultado:
             return'Incorrecto \n {0}+{1}={2}'.format(a,b,a+b)
        else:
            return 'CORRECTO'


    def RESTA(self,a,b, resultado):
        if a-b != resultado:
             return'Incorrecto \n {0}-{1}={2}'.format(a,b,a-b)
        else:
            return 'CORRECTO'



    def MULTIPLICACION(self, a,b, resultado):
        if int(a*b) != resultado:
            return'Incorrecto \n {0}*{1}={2}'.format(a,b,a*b)
        else:
            return 'CORRECTO'



    def DIVISION(self,a,b, resultado):
        if int(a/b) != resultado:
             return'Incorrecto \n {0}/{1}={2}'.format(a,b,int(a/b))
        else:
            return 'CORRECTO'



if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()
