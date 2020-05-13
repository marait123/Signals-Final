import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import sounddevice as sd
import time
import matplotlib.pyplot as plt

duration_s = 2
# a. read the the file audio1.wav
fs, audio = wavfile.read('./audio1.wav')
 
# let's add echo to the sound
# impulse response has 2001
# b. find y(t) = x(t)+.9 * x(t-.25) + .8 * x(t-.5) + .7 * x(t-.75)
secondSize = fs

 
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

print('hi')
