##### Importación de librería y funciones ########
import numpy as np
from scipy.io.wavfile import read
from scipy.fftpack import fft
from scipy.fftpack import ifft
from os.path import isfile
import matplotlib.pyplot as plt
import re


######## Definición de Funciones ##############

def normalizarDatosInfo(data, frecuenciaMuestreo):
	largoData= len(data) #Obtenemos el la cantidad de datos obtenidos del audio
	intervalo = np.linspace(largoData) # Generamos un arreglo de valores para el intervalo de tiempo
	periodo = largoData/frecuenciaMuestreo #Encontramos el valor del Período
	rangoFrec = intervalo/periodo #Nuevo arreglo con el intervalo de frecuencias
	rangoFrec = rangoFrec[range(round(largoData/2))] 

	newdata = fft(data)/largoData
	newdata = newdata[range(round(largoData/2))]

	
	return rangoFrec, newdata

def graficarSonidoEnDominioDeTiempo(info,frecuenciaMuestreo):
	print("Frecuencia de muestreo del audio: " + str(frecuenciaMuestreo))
	dimension = len(info)
	print("Dimensión de la información: "+str(dimension))
	print(info)	
	frq, newdata = normalizarDatosInfo(info,frecuenciaMuestreo)
	plt.plot(frq,newdata,'r' )
	plt.show()



############## Bloque Main ################
patron_punto_wav = re.compile(".*\.wav$")
archivo = input("Ingrese el nombre de archivo de sonido (*.wav): ")
while not isfile(archivo):
	print("El archivo \""+archivo+"\" no existe")
	archivo = input("Ingrese el nombre de archivo de sonido (*.wav): ")
	comprobacion = patron_punto_wav.match(archivo)
	while(comprobacion == None):
		print(" Agregue la extensión *.wav al archivo: \""+archivo+"\"")
		archivo = input("Ingrese el nombre de archivo de sonido (*.wav): ")
		comprobacion = patron_punto_wav.match(archivo)

frecuenciaMuestreo, info = read(archivo)

graficarSonidoEnDominioDeTiempo(info,frecuenciaMuestreo)

