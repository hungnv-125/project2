import noisereduce as nr
from scipy.io import wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import librosa
import IPython
# load data
rate, data = wavfile.read("testfile.wav")
# data, rate = librosa.load("test_data/hung1.wav")
# select section of data that is noise
# noisy_part = data[0:20000]
# perform noise reduction
# reduced_noise = nr.reduce_noise(audio_clip=data, noise_clip=data, verbose=True)
# wavfile.write("F:/client1/nguyen_thien_nhan.wav", rate, reduced_noise)
#
print(rate)