from pip._vendor.six import byte2int

__author__ = 'Benja'


def file_to_bytes(path):
    # rb = read binary
    with open(path, 'rb') as file:
        return bytearray(file.read())


def new_file(nombre, bytes):
    # rb = read binary
    with open(nombre, 'wb') as file:
        file.write(bytes)


def actividad(nombre_archivo):
    a = file_to_bytes(nombre_archivo)
    primero = a[:44]
    segundo = a[:44]
    j = 0
    for i in a[44:]:
        if j % 2 == 0:
            primero.append(i)
        else:
            segundo.append(i)
        j += 1
    c1 = new_file('1_' + nombre_archivo, primero)
    c2 = new_file('2_' + nombre_archivo, segundo)


def bonus(nombre_archivo, frecuencia):
    a = file_to_bytes(nombre_archivo)
    b = frecuencia.to_bytes(4, byteorder='little')
    a[24:28] = b
    print(a[25:28])
    a[28:32] = b
    new_file('mod_{}'.format(frecuencia) + nombre_archivo, a)
    actividad('mod_{}'.format(frecuencia) + nombre_archivo)


actividad("musica.wav") #retorna 1_musica.wav y 2_musica.wav
b = bonus('audio.wav', 11025) #retorna 1_mod_11025audio.wav y 2_mod_11025audio.wav
c = bonus('audio.wav', 22050) #retorna 1_mod_22050audio.wav y 2_mod_22050audio.wav

#ambos bonus tambien crean mod_11025audio.wav y mod_22050audio.wav que son los archivos que se
#le entrega a la funcion de la actividad para separar