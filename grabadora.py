import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from scipy.io import wavfile
from datetime import datetime


try:
    tiempo = int(input("Ingresa el tiempo de grabacion en segundos:"))
except Exception as e:
    print('Ingrese un valor correcto')
    exit()

try:
    nombre = str(input("¿Cual es el nombre de la grabacion?:"))
    print(f'El nombre de la grabacion sera: {nombre}.wav')
except Exception as e:
    print('Ingrese un nombre valido')
    exit()

fs = 44100
try:
    myrecording = sd.rec(int(tiempo*fs),
    samplerate = fs, channels= 1)
    print('Grabando...')
    sd.wait()
    write(nombre + '.wav',fs,myrecording)
    print('Grabacion finalizada')


    samplingFrequency, signalData = wavfile.read(nombre +'.wav')

    plt.title('-Espectro de Frecuencias- '+ str(datetime.now()))
    plt.specgram(signalData,Fs=samplingFrequency)
    plt.xlabel('Tiempo')
    plt.ylabel('Frecuencia')

    plt.show()

except Exception as e:
    print('error, intentelo mas tarde')
