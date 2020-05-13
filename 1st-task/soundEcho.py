import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import sounddevice as sd
import time
import matplotlib.pyplot as plt
import os


duration_s = 4
# a. read the the file audio1.wav
fs, audio = wavfile.read('./audio1.wav')
 
# let's add echo to the sound
# impulse response has 2001
# b. find y(t) = x(t)+.9 * x(t-.25) + .8 * x(t-.5) + .7 * x(t-.75)
audioLength = len(audio)
secondSize = fs
x25 = np.zeros(audioLength + fs)
x25[int(.25 * fs):int(audioLength+.25*fs)] =.9* audio
x50 = np.zeros(audioLength + fs)
x50[int(.5 * fs):int(audioLength+.5*fs)] = .8*audio

x75 = np.zeros(audioLength + fs)
x75[int(.75 * fs):int(audioLength+.75*fs)] = .7*audio

y = (list(audio)+list(np.zeros(fs))) + x25 + x50 + x75
print(type(y))

sd.play(y, fs)
plt.plot(y)
plt.plot(audio)
plt.show()
time.sleep(duration_s)

# C. find and plot the impulse response of the echo generation system
# h is the impluse response of the system
h = np.zeros(secondSize)
h[int (0 * secondSize)] = 1
h[int (.25 * secondSize)] = .9
h[int (.5 * secondSize)] = .8
h[int (.75 * secondSize)] = .7
# plot h
plt.plot(h)

plt.show()
echoedAudio = np.convolve(audio, h)
sd.play(echoedAudio, fs)
time.sleep(duration_s)
sd.stop()

