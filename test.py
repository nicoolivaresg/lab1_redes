from numpy import sin, linspace, pi
from pylab import plot, show, title, xlabel, ylabel, subplot
from scipy import fft, arange
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
	 
 	plot(frq,abs(Y),'r') # plotting the spectrum
 	xlabel('Freq (Hz)')
 	ylabel('|Y(freq)|')

freq, info = read("lab1-2.wav")

Fs = 150.0;  # sampling rate
Ts =len(info)/freq; # sampling interval
t = linspace(0,Ts,len(info)) # time vector

#ff = 5;   # frequency of the signal
#y = sin(2*pi*ff*t)

subplot(2,1,1)
plot(t,info)
xlabel('Time')
ylabel('Amplitude')
subplot(2,1,2)
plotSpectrum(info,freq)
show()