from scipy.io import wavfile
import numpy as np
import sounddevice as sd
import time
import matplotlib.pyplot as plt
from scipy import fft,ifft

duration_s = 4
# a. read the the file audio1.wav
fs, audio = wavfile.read('./audio1.wav')
# let's add echo to the sound
# impulse response has 2001
# b. find y(t) = x(t)+.9 * x(t-.25) + .8 * x(t-.5) + .7 * x(t-.75)
audioLength = len(audio)
secondSize = fs
x25 = np.zeros(audioLength + fs)
x25[int(.25 * fs):int(audioLength + .25 * fs)] = .9 * audio
x50 = np.zeros(audioLength + fs)
x50[int(.5 * fs):int(audioLength + .5 * fs)] = .8 * audio

x75 = np.zeros(audioLength + fs)
x75[int(.75 * fs):int(audioLength + .75 * fs)] = .7 * audio

y = (list(audio) + list(np.zeros(fs))) + x25 + x50 + x75

sd.play(y[0:audioLength].astype(np.dtype('i2')), fs)
plt.plot(y)
plt.plot(audio)
plt.show()
time.sleep(duration_s)

#output the audio_with_echo_after_using_given_formula.wav
wavfile.write("audio_with_echo_after_using_given_formula.wav",fs,y[0:audioLength].astype(np.dtype('i2')))

# C. find and plot the impulse response of the echo generation system
# h is the impluse response of the system
h = np.zeros(secondSize)
h[int(0 * secondSize)] = 1
h[int(.25 * secondSize)] = .9
h[int(.5 * secondSize)] = .8
h[int(.75 * secondSize)] = .7

# plot h
plt.plot(h)

#output impulse_response.png
plt.savefig('sample-graph.png')

plt.show()


#ly=lx+lh-1
h_len=len(h)
audio_len=len(audio)

N=len(audio)+len(h)-1
h=list(h)+list(np.zeros(N-len(h)))
h=np.array(h)
audio=list(audio)+list(np.zeros(N-len(audio)))
audio=np.array(audio)

#convolve the audio with the impulse response to generate echo
echoedAudio = np.convolve(audio, h)
sd.play(echoedAudio[0:audioLength].astype(np.dtype('i2')), fs)
time.sleep(duration_s)

#output the audio_with_echo_after_convolution.wav
wavfile.write("audio_with_echo_after_convolution.wav",fs,echoedAudio[0:audioLength].astype(np.dtype('i2')))

#get x[n] given y[n](echoedAudio) and h[n] (h)
xn_fft=fft.fft(echoedAudio,N)/fft.fft(h,N)
xn=fft.ifft(xn_fft)
xn=np.real(xn)
xn=np.around(xn)
xn=np.array(xn)
xn=xn[0:audioLength]
xn=xn.astype(np.dtype('i2'))

#output the audio_after_echo_removal.wav
wavfile.write("audio_after_echo_removal.wav",fs,xn)

