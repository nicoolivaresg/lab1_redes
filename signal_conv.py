##### Importación de librería y funciones ########
import numpy as np
from scipy.io.wavfile import read, write
from scipy.fftpack import fft, ifft
from os.path import isfile
import matplotlib.pyplot as plt
import re


####### Constantes y variables globales #######

TITLE1 = "a"
TITLE2 = "b"
TITLE3 = "c"
TITLE4 = "d"
TITLE5 = "e"

XLABEL1 = "aa"
XLABEL2 = "bb"
XLABEL3 = "cc"
XLABEL4 = "dd"
XLABEL5 = "ee"

YLABEL1 = "aaa"
YLABEL2 = "bbb"
YLABEL3 = "ccc"
YLABEL4 = "ddd"
YLABEL5 = "eee"

DPI = 100
FIGURE_WIDTH = 8
FIGURE_HEIGHT = 3

figureCounter = 0

########## Definición de Funciones ############

# Funcion que grafica los datos en ydata y xdata, y escribe los nombres del eje x, eje y,
# y el titulo de una figura. Esta figura la guarda en un archivo con el nombre filename.
# Entrada:
#	filename - Nombre del archivo en donde se guarda la figura.
#	title	 - Titulo de la figura.
#	ylabel	 - Etiqueta del eje y.
#	xlabel	 - Etiqueta del eje x.
#	ydata	 - Datos del eje y.
#	xdata	 - Datos del eje X, por defecto es un arreglo vacío que luego se cambia por un
#			   arreglo desde 0 hasta largo de ydata - 1
#	color	 - Color de la figura en el grafico, por defecto es azul (blue).
def graficar(filename, title, ylabel, xlabel, ydata, xdata=np.array([]), color='b'):
	if xdata.size == 0:
		xdata = np.arange(len(ydata))

	plt.figure(figsize=(FIGURE_WIDTH,FIGURE_HEIGHT), dpi=DPI)
	plt.plot(xdata, ydata, color)
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.savefig(filename, bbox_inches='tight')
	plt.clf()

def openWavFile(filename):
	frecuencia, datos = read(filename)
	n = len(datos)
	Ts = n / frecuencia; # Intervalo de tiempo
	times = np.linspace(0, Ts, n) # Tiempo en segundos para cada dato de 'datos'
	return (frecuencia, datos, times)

def fourierTransform(data, frequency):
	n = len(data)
	Ts = n / frequency
	fftValues = fft(data) / n # Computacion y normalizacion
	fftSamples = np.fft.fftfreq(n, 1/frequency)

	return (fftValues, fftSamples)

def truncateFft(fftValues):
	n = len(fftValues)
	maxFreqI = 0
	maxFreq = 0
	for i in range(n):
		if fftValues[i] > maxFreq:
			maxFreq = fftValues[i]
			maxFreqI = i


	leftI = int(maxFreqI - (n*0.15))
	rightI = int(maxFreqI + (n*0.15))

	fftTruncada = np.array([0]*n)

	if (leftI < 0):
		for i in range(rightI):
			fftTruncada[i] = fftValues[i]

		for j in range(n+leftI, n):
			fftTruncada[j] = fftValues[j]
	elif (rightI >= n):
		for i in range(rightI-n):
			fftTruncada[i] = fftValues[i]

		for j in range(leftI, n):
			fftTruncada[j] = fftValues[j]
	else:
		for i in range(leftI, rightI):
			fftTruncada[i] = fftValues[i]

	return fftTruncada

def fourierInverse(fftValues):
	return ifft(fftValues)*len(fftValues)

def processFile(filename):
	global figureCounter
	figureCounter += 1
	frecuencia, datos, times = openWavFile(filename)
	fftNormalizada, fftSamples = fourierTransform(datos, frecuencia)
	fftTruncada = truncateFft(fftNormalizada)
	fftNormalizadaInversa = fourierInverse(fftNormalizada)
	fftTruncadaInversa = fourierInverse(fftTruncada)

	graficar(str(figureCounter) + "-1.png", TITLE1, YLABEL1, XLABEL1, datos, times)
	graficar(str(figureCounter) + "-2.png", TITLE1, YLABEL1, XLABEL1, abs(fftNormalizada), fftSamples)
	graficar(str(figureCounter) + "-3.png", TITLE1, YLABEL1, XLABEL1, fftNormalizadaInversa, times)
	graficar(str(figureCounter) + "-4.png", TITLE1, YLABEL1, XLABEL1, abs(fftTruncada), fftSamples)
	graficar(str(figureCounter) + "-5.png", TITLE1, YLABEL1, XLABEL1, fftTruncadaInversa, times)

	write(filename[:len(filename)-4] + "-inversed.wav", frecuencia, fftTruncadaInversa.astype(datos.dtype))


################ Bloque Main ##################
"""
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

processFile(archivo)
"""
processFile("lab1-1.wav")
processFile("lab1-2.wav")