import wave, numpy as np, matplotlib.pyplot as plt

wf = wave.open("music.wav", "rb")
frames = wf.readframes(-1)
signal = np.frombuffer(frames, dtype=np.int16)

plt.plot(signal[:1000])
plt.title("Waveform")
plt.show()
