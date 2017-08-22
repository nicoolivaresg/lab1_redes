
from numpy import sin, linspace, pi
from pylab import plot, show, title, xlabel, ylabel, subplot
from scipy import ifft, fft, arange
from scipy.io.wavfile import read



def plotSpectrum(y,Fs):
 	"""
 	Plots a Single-Sided Amplitude Spectrum of y(t)
 	"""
 	n = len(y) # length of the signal
 	k = arange(n)
 	T = n/Fs
 	frq = k/T # two sides frequency range
 	frq = frq[range(round(n/2))] # one side frequency range

 	Y = fft(y)/n # fft computing and normalization
 	Y = Y[range(round(n/2))]
	 
 	#plot(frq,abs(Y),'r') # plotting the spectrum
 	#xlabel('Freq (Hz)')
 	#ylabel('|Y(freq)|')

 	maxFreqI = 0;
 	maxFreq = 0;
 	for i in range(len(Y)):
 		if Y[i] > maxFreq:
 			maxFreq = Y[i]
 			maxFreqI = i

 	n = len(Y)
 	left = round(maxFreqI - maxFreqI*0.15)
 	if(left < 0):
 		left = 0
 	right = round(maxFreqI + maxFreqI*0.15)
 	if(right >= n):
 		right = n-1

 	shortSpectrum = Y
 	for i in range(n):
 		if(i < left or i > right):
 			shortSpectrum[i] = 0
 	print (maxFreq, n, left, right, len(shortSpectrum))

 	plot(frq, abs(shortSpectrum), 'r')
 	xlabel('Freq (Hz)')
 	ylabel('|Y(freq)|')

 	return shortSpectrum

freq, info = read("lab1-1.wav")

Ts =len(info)/freq; # sampling interval
t = linspace(0,Ts,len(info)) # time vector

#ff = 5;   # frequency of the signal
#y = sin(2*pi*ff*t)

subplot(3,1,1)
plot(t,info)
xlabel('Time')
ylabel('Amplitude')
subplot(3,1,2)
shortSpectrum = plotSpectrum(info,freq)
subplot(3,1,3)
t2 = linspace(0, Ts, len(shortSpectrum))
plot(t2,ifft(shortSpectrum))
xlabel('Time')
ylabel('Amplitude')
show()