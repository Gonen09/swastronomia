from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math as mt


def array_test():

    pixel = []
    pixel.append(3)
    pixel.append(8)
    pixel.append(9)
    pixel.append(2)

    print pixel
    del pixel[:]
    print pixel


def array_opetions():

    pixel = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print pixel

    vector = [x * 3 for x in pixel]

    print vector

    salida = [mt.sqrt(x) for x in vector]

    print salida


def info_fits(cubo_fits):
    # Coordenadas del cubo [Z,Y,X]

    naxis = 0
    naxis1 = 0
    naxis2 = 0
    naxis3 = 0

    hdulist = fits.open(cubo_fits)
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


def pixel_fits(cubo_fits, pixel_x, pixel_y):
    hdulist = fits.open(cubo_fits)
    cubo = hdulist[0].data  # hdulit[0] = PrimaryHDU
    hdulist.close()
    return cubo[:, pixel_y, pixel_x]


def graficar(datos):
    plt.plot(datos)
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

    print 'Ejes(naxis) => X = ', naxis1, ' Y = ', naxis2, ' Z = ', naxis3
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


def crear_archivo(nombre):
    archi = open(nombre, 'w')
    archi.close()


def main():

    array_opetions()

main()
