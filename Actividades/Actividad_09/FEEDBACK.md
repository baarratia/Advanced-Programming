# [Actividad 9](https://github.com/IIC2233-2015-1/syllabus/tree/master/Actividades%20en%20Clases/Actividad%2009)

### Distribución de puntajes

Requerimientos (**R**):

* **(1.0 pts)** R1: Nombres bien escritos
* **(2.0 pts)** R2: MetaPersona
* **(1.5 pts)** R3: MetaEmpresa: `nuevo_empleado`
* **(1.5 pts)** R4: MetaEmpresa: `subir_sueldo`
* **(2.0 pts)** B (Bonus).

**Además, se descontará (0.5) puntos si no sigue formato de entrega.**

### Obtenido por el alumno
| R1 | R2 | R3 | R4 | Bonus | Descuento |
|:---|:---|:---|:---|-------|:----------|
| 0.5  | 1  | 1.5  | 1  | 0     | 0         |

| Nota |
|:-----|
| **5.0** |

### Comentarios
* Bien verificar nombre de la clase, pero te faltaron casos :c :
```
        if nombre == 'Persona':
```
debería ser algo como:
```
        if nombre in ['Persona','Empleado,'Jefe']:
```
y en `MetaEmpresa` deberías retornar uns instancia del objeto ssi `nombre==Empresa`:
````
def __new__(meta, nombre, base_clases, diccionario):
        if nombre == "Empresa":
	...
	"""
	Falta identar la siguiente parte
	"""
	return super().__new__(meta, nombre, base_clases, diccionario)
```

* Bien la función `hacer_tarea`, pero no modificaste el comportamiento de llamada a la instancia:
```
funcion = lambda self, tarea: print('{0} está haciendo la siguiente tarea: {1}'.format(self.nombre, tarea))
            diccionario.update(dict({'hacer_tarea': funcion}))
```
debería ser algo como:
```
hacer_tarea = lambda self, tarea: print('{0} está haciendo la siguiente tarea: {1}'.format(self.nombre, tarea))
            diccionario.update(dict({'__call__': hacer_tarea}))
```
* En esta parte:
```
        diccionario["subir_sueldo"]=subir_sueldo()
```
estás llamando a la función y no estás referenciando a la función en sí (el objeto `subir_sueldo`). Deberías haber puesto algo como:
```
        diccionario["subir_sueldo"]=subir_sueldo
```