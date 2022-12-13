__author__ = 'Benja'


class MetaPersona(type):
    def __new__(meta, nombre, clases_base, diccionario):
        if nombre == 'Persona':
            funcion = lambda self, tarea: print('{0} está haciendo la siguiente tarea: {1}'.format(self.nombre, tarea))
            diccionario.update(dict({'hacer_tarea': funcion}))
            print(diccionario)
            return super().__new__(meta, nombre, clases_base, diccionario)
        else:
            pass

class MetaEmpresa(type):
    def __new__(meta, nombre, base_clases, diccionario):
        if nombre == "Empresa":
            def nuevo_empleado(self,empleado):
                self.empleados[empleado.id_empleado] = empleado
            diccionario["nuevo_empleado"]= nuevo_empleado

        def subir_sueldo(self, id,password):
                x = self.empleados.get(id, "NO")
                if x!= 'NO':
                    if password == 'Tu jefecito lindo':
                        self.empleados[id].sueldo += 1
                        print("Sueldo Subido")
                    else:
                        print("Contraseña Incorrecta")
                else:
                    print("ID no valida")
        diccionario["subir_sueldo"]=subir_sueldo()


        return super().__new__(meta, nombre, base_clases, diccionario)