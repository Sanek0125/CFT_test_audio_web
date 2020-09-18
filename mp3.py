
import librosa

import matplotlib.pyplot as plt
import librosa.display

def graph_builder(audio_data):
    

    x , sr = librosa.load(audio_data)
    # print(type(x), type(sr))
    # #<class 'numpy.ndarray'> <class 'int'> 
    # print(x.shape, sr)
    # #(94316,) 22050, transporter05.wav

    #plt.figure(figsize=(14, 5))
    librosa.display.waveplot(x, sr=sr)
    plt.savefig('books_read.png')










# import time
# import pygame
# pygame.init()
# pygame.mixer.music.load('MaryGu.mp3')
# clock = pygame.time.Clock()
# pygame.mixer.music.play()

# input()

# pygame.mixer.music.stop()



# # import IPython.display as ipd
# # ipd.Audio(audio_data)

