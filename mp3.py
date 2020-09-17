import librosa
audio_data = '/../../gruesome.wav'
x , sr = librosa.load(audio_data)
print(type(x), type(sr))
#<class 'numpy.ndarray'> <class 'int'>
print(x.shape, sr)
#(94316,) 22050

import IPython.display as ipd
ipd.Audio(audio_data)
