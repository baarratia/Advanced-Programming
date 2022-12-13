# Actividad 18
### Distribución de puntajes

- **R1 (3.0 puntos):** Crear la interfaz con todos sus widgets en Qt Designer
- **R2 (1.0 puntos):** Al solicitar una nueva operación, se generan número aleatorios (coherentes con la
operación) y son mostrados en la interfaz
- **R3 (1.0 puntos):** Al revisar la respuesta, ésta es verificada correctamente según lo que respondió el usuario y se entrega el feedback correcto (i.e: avisa cuado es correcto o incorrecto).
- **R4 (1.0 puntos):** Informar al usuario cuál es el valor correcto de la operación.


### Obtenido por el alumno

| R1 | R2 | R3 | R4 | Descuento |
|:--------|:--------|:--------|:--------|:--------|
| 3 | 0.7 | 0.7 | 1 | 0 |

| Nota |
|:-----|
| **6.4** |

### Comentarios
* Este código hace que tu juego sea poco random. Esto es solo necesario para las restas. 
```python
def asignar(self):
    a = random.randrange(1, 20)
    if a != 1:
        b = random.randrange(1, a)
    else:
        b = 1
    return a,b
```
* Solo se trabaja con números del 1 al 20. No puedes tener operaciones con resultados mayores a 20
* Solo hay un intento por operación
