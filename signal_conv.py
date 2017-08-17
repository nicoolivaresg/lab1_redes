##### Importación de librería y funciones ########
import numpy as np
from scipy.io.wavfile import read
from scipy.fftpack import fft
from scipy.fftpack import ifft
from os.path import isfile
import matplotlib.pyplot as plt
import re


######## Definición de Funciones ##############
"""
def normalizarDatosInfo(data,LimiteInferior,LimiteSuperior):
	ValorInferiorEntrada = np.amin(data)
	ValorSuperiorEntrada = np.amax(data)
	print(str(ValorSuperiorEntrada))
	relacion = (LimiteSuperior - LimiteInferior)/(ValorSuperiorEntrada- ValorInferiorEntrada)
	comp = ValorInferiorEntrada * relacion
	DatosNormalizados = relacion * data - comp
	return DatosNormalizados
"""
def graficarSonidoEnDominioDeTiempo(info,frecuenciaMuestreo):
	print("Frecuencia de muestreo del audio: " + str(frecuenciaMuestreo))
	dimension = len(info)
	print("Dimensión de la información: "+str(dimension))
	print(info)
	plt.plot(info )
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
#newdata = normalizarDatosInfo(info,-100,100)
graficarSonidoEnDominioDeTiempo(info,frecuenciaMuestreo)

