import numpy as np
from numpy import sin, linspace, pi
from pylab import plot, show, title, xlabel, ylabel, subplot
from scipy import *
from scipy.io.wavfile import read, write



def plotSpectrum(y,Fs):
 	"""
 	Plots a Single-Sided Amplitude Spectrum of y(t)
 	"""
 	n = len(y) # length of the signal
 	k = arange(n)
 	T = n/Fs
 	frq = np.fft.fftfreq(n, 1/Fs)

 	Y = fft(y)/n # fft computing and normalization
 	#Y = Y[range(round(n/2))]
	 
 	#plot(frq,abs(Y),'r') # plotting the spectrum
 	#xlabel('Freq (Hz)')
 	#ylabel('|Y(freq)|')
 	
 	maxFreqIl = 0
 	maxFreqIr = 0
 	maxFreq = 0
 	for i in range(len(Y)):
 		if int(Y[i]) > maxFreq:
 			maxFreq = int(Y[i])
 			maxFreqIl = i

 	for i in range(len(Y)):
 		if int(Y[i]) == maxFreq and i != maxFreqIl:
 			maxFreqIr = i
 			break

 	left = maxFreqIl + 1
 	right = maxFreqIr - 1

 	shortSpectrum = Y
 	for i in range(int(n/2)):
 		if i > left:
 			shortSpectrum[i] = 0

 	for i in range(int(n/2)+1, n):
 		if i < right:
 			shortSpectrum[i] = 0

 	plot(frq, abs(shortSpectrum), 'r')
 	xlabel('Frecuencia (Hz)')
 	ylabel('Amplitud [dB]')

 	return shortSpectrum

filename = "lab1-1"
freq, info = read(filename + ".wav")

Ts =len(info)/freq; # sampling interval
t = linspace(0,Ts,len(info)) # time vector

#ff = 5;   # frequency of the signal
#y = sin(2*pi*ff*t)

subplot(3,1,1)
plot(t,info)
xlabel('Tiempo [s]')
ylabel('Amplitud')
subplot(3,1,2)
shortSpectrum = plotSpectrum(info,freq)
subplot(3,1,3)
Z = ifft(shortSpectrum)*len(info) #desnornalizar
#print(shortSpectrum)
#print(Z)
plot(t, Z, 'g')
xlabel('Tiempo [s]')
ylabel('Amplitud')
show()

write(filename + "-inverse.wav", freq, Z.astype(info.dtype))