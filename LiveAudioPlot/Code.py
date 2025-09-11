import sounddevice as sd
import numpy as np

def callback(indata, frames, time, status):
    volume = int(np.linalg.norm(indata) * 50)
    print("█" * volume)

with sd.InputStream(callback=callback):
    sd.sleep(5000)  # Run for 5s
