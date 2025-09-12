# WaveDrawer

WaveDrawer is a Python program that visualizes the waveform of a WAV audio file. It reads the audio data and plots the first 1000 samples using matplotlib, allowing you to see the shape of the sound.

## Features
- Loads a WAV file and extracts audio samples
- Plots the waveform of the first 1000 samples
- Displays the plot with a title

## Requirements
- Python 3.x
- numpy
- matplotlib

## Installation
Install the required Python packages:
```powershell
pip install numpy matplotlib
```

## Usage
1. Place your WAV file (e.g., `music.wav`) in the program directory.
2. Run the script:
   ```powershell
   python Code.py
   ```
3. A plot window will appear showing the waveform of the first 1000 samples.

## Notes
- The script expects a file named `music.wav` in the same directory. You can change the filename in the code if needed.
- Only the first 1000 samples are plotted for quick visualization.
- Works with standard PCM WAV files.

## License
This project is provided for educational purposes.
