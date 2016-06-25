from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math as mt
from copy import deepcopy

# Constantes definidas por el astronomo
GANANCIA = 2.1
RUIDO = 4
TOLERANCIA_RUIDO = 3


def info_fits(nombre_archivo):

    # Coordenadas del cubo [Z,Y,X]

    naxis1 = 0
    naxis2 = 0
    naxis3 = 0

    hdulist = fits.open(nombre_archivo)
    hdulist.info()

    cubo = hdulist[0].data  # hdulit[0] = PrimaryHDU

    naxis = hdulist[0].header['naxis']

    print 'Numero de dimensiones = ', naxis

    if naxis == 1:
        naxis1 = hdulist[0].header['naxis1']
    if naxis == 2:
        naxis1 = hdulist[0].header['naxis1']
        naxis2 = hdulist[0].header['naxis2']
    if naxis == 3:
        naxis1 = hdulist[0].header['naxis1']
        naxis2 = hdulist[0].header['naxis2']
        naxis3 = hdulist[0].header['naxis3']

    print 'Ejes (naxis) => X = ', naxis1, ' Y = ', naxis2, ' Z = ', naxis3

    print
    print 'Datos [0,0,0] = ', cubo[0, 0, 0]
    print 'Datos [40,199,199] = ', cubo[39, 199, 199]
    print
    print 'Datos del cubo eje z pixel 0x0'
    print
    print cubo[:, 0, 0]

    # for i in range (0,40,1):  #cubo[:,0,0]
    # print cubo[i,0,0]

    hdulist.close()


def graficar_z(datos):

    plt.plot(datos)
    plt.title('Eje Z')
    plt.ylabel('Intensidad')
    plt.xlabel('Longitud de onda')
    plt.show()


def graficar_vs(dato1, dato2):

    plt.plot(dato1)
    plt.plot(dato2)
    plt.title('Eje Z')
    plt.ylabel('Intensidad')
    plt.xlabel('Longitud de onda')
    plt.show()


def estadistica(datos):

    print
    print 'Estadistica de los datos'
    print '------------------------'
    print
    print 'Minimo:', np.min(datos)
    print
    print 'Maximo:', np.max(datos)
    print
    print 'Media:', np.mean(datos)
    print
    print 'Desviacion estandar:', np.std(datos)
    print


def crear_archivo(nombre):

    archi = open(nombre, 'w')
    archi.close()


def fits_to_csv():

    # Inicializar variables

    crear_archivo('csvfits.csv')

    naxis = 0
    naxis1 = 0
    naxis2 = 0
    naxis3 = 0

    # Cargar cubo fits

    hdulist = fits.open('cubo_ing_comp.fits')
    cubo = hdulist[0].data
    naxis = hdulist[0].header['naxis']

    # Cargar dimensiones del cubo

    if naxis == 1:
        naxis1 = hdulist[0].header['naxis1']
    if naxis == 2:
        naxis1 = hdulist[0].header['naxis1']
        naxis2 = hdulist[0].header['naxis2']
    if naxis == 3:
        naxis1 = hdulist[0].header['naxis1']
        naxis2 = hdulist[0].header['naxis2']
        naxis3 = hdulist[0].header['naxis3']

    # print 'Ejes (naxis) => X = ', naxis1, ' Y = ', naxis2, ' Z = ', naxis3

    archi = open('csvfits.csv', 'a')
    salida = ''

    for x in range(0, naxis1, 1):
        for y in range(0, naxis2, 1):
            for z in range(0, naxis3 - 1, 1):
                salida = salida + str(cubo[z, y, x]) + ':'
            salida = salida + str(cubo[naxis3 - 1, y, x]) + ';'
        archi.write(salida + '\n')
        salida = ''

    hdulist.close()
    archi.close()


def pixel_fits(cubo, pixel_x, pixel_y):

    vector = deepcopy(cubo[:, pixel_y, pixel_x])
    return vector


def pixel_electron(vector):

    # Este modulo convertira un perfile del cubo de datos en electrones

    arreglo = deepcopy(vector)
    longitud_vector = len(arreglo)
    # print "Longitud vector = ", longitud_vector

    indicador = False

    for v in range(0, longitud_vector, 1):

        if arreglo[v] < 0:

            arreglo[v] = mt.fabs(arreglo[v])
            indicador = True

        # print "valor = ", vector[v]

        amplificado = arreglo[v] * GANANCIA
        # print "amplificado = ", amplificado

        raiz = mt.sqrt(amplificado)
        # print "raiz = ", raiz

        final = amplificado / raiz
        # print "final = ", final
        # print

        if indicador:

            final *= -1
            indicador = False

        arreglo[v] = final

    return arreglo


def pixel_quitar_ruido(vector):

    arreglo = deepcopy(vector)

    longitud_vector = len(arreglo)

    for v in range(0, longitud_vector, 1):
        if arreglo[v] > 0:
            arreglo[v] -= RUIDO

    return arreglo


def pixel_normalizar(vector):

    arreglo = deepcopy(vector)
    longitud_vector = len(arreglo)
    maximo = np.max(vector)

    # print arreglo
    # print "maximo", maximo

    for v in range(0, longitud_vector, 1):
        arreglo[v] /= maximo

    return arreglo


def transformar_cubo(cubo, dim_x, dim_y):

    dim_x -= 1
    dim_y -= 1

    for x in range(0, dim_x, 1):
        for y in range(0, dim_y, 1):

            # print 'Coordenada [', x, ',', y, ']'
            vector = pixel_fits(cubo, x, y)

            # print "Pixel original"
            # print vector
            # print
            vector = pixel_electron(vector)
            # print "Pixel electrico"
            # print vector
            # print
            # vector = pixel_quitar_ruido(vector)
            # print "Pixel sin ruido"
            # print vector
            # print
            # vector = pixel_normalizar(vector)
            # print "Pixel normalizado"
            # print vector
            # print

            plt.plot(vector)

            cubo[:, dim_y, dim_x] = deepcopy(vector)

            # print 'cubo'
            # print cubo[:, dim_y, dim_x]
            # print
            vector = []
            # print vector


    plt.title('Eje Z')
    plt.ylabel('Intensidad')
    plt.xlabel('Longitud de onda')
    plt.show()

    return cubo


def fits_test():

    # Obtener cubo
    archivo = 'cubo_ing_comp.fits'
    hdulist = fits.open(archivo)
    cubo = hdulist[0].data  # cubo fits nomal

    naxis1 = hdulist[0].header['naxis1']  # Dimension X
    naxis2 = hdulist[0].header['naxis2']  # Dimension y
    naxis3 = hdulist[0].header['naxis3']  # Dimension z

    pixelito = pixel_fits(cubo, 0, 0)
    epixel = pixel_electron(pixelito)

    print "Pixel original"
    print pixelito
    print
    print "Pixel electrico"
    print epixel

    graficar_z(pixelito)
    graficar_z(epixel)

    graficar_vs(pixelito, epixel)

    srpixel = pixel_quitar_ruido(epixel)
    print
    print "Pixel sin ruido"
    print srpixel

    graficar_z(srpixel)

    graficar_vs(epixel, srpixel)

    nrpixel = pixel_normalizar(srpixel)

    print
    print "Pixel normalizado"
    print nrpixel
    graficar_z(nrpixel)

    graficar_vs(srpixel, nrpixel)


def main():

    # Obtener cubo
    archivo = 'cubo_ing_comp.fits'
    hdulist = fits.open(archivo)
    cubo = hdulist[0].data  # cubo fits nomal

    naxis1 = hdulist[0].header['naxis1']  # Dimension X
    naxis2 = hdulist[0].header['naxis2']  # Dimension y
    naxis3 = hdulist[0].header['naxis3']  # Dimension z

    print 'inicio'

    cubo = transformar_cubo(cubo, naxis1, naxis2)

    print 'fin'

    # vector = pixel_fits(cubo, 150, 150)
    # print vector
    # graficar_z(vector)

    fits_test()

main()
