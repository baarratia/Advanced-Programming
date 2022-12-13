# Actividad 14
### Distribución de puntajes

Errores en orden de aparición.

- **R1 (1 puntos):** Error sobre letra G.
- **R2 (1 puntos):** Error sobre 1 dividido 0.
- **R3 (1 puntos):** Error sobre `a`.
- **R4 (1 puntos):** Error sobre `StopIteration`.
- **R5 (1 puntos):** Error sobre `ValueError`.
- **R6 (1 puntos):** Error sobre sintaxis.


### Obtenido por el alumno

| R1 | R2 | R3 | R4 | R5 | R6 | Descuento |
|:---|:---|:---|:---|:---|:---|:----------|
| 1  | 1  | 0  | 1  | 0  | 0  | 0         |

| Nota |
|:-----|
| **4.0** |

### Comentarios
* Esto está mal usado.
```python
if self.letras_especiales.get(letra, 'NO') == 'NO':
    self.letras_especiales[letra] = valor
```
``dict.get(key, default=x)`` lo que hace es asignar el valor x a key. Si querías saber si letra estaba dentro de las letras especiales, tendrías que haber hecho
```python
if letra in self.letras_especiales.keys():
    ...
```
* ¿Qué error es este? El enunciado no decía que debías hacer esto.
```python
try:
    resultado = operador1 + operador2
except TypeError:
    return print('[ERROR] TypeError \nno se pueden sumar operadores de distinto tipo')
```
* ¿Qué pasa si el nombre de cada error cambia? En tu código debería cambiarlo cada una de las veces que lanzas una excepción. 