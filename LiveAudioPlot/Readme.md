# LiveAudioPlot

LiveAudioPlot is a simple Python program that visualizes live microphone input as a real-time ASCII bar graph in the terminal. The height of the bar represents the audio volume detected from the microphone.

## Features
- Captures live audio from your default microphone
- Displays volume as a dynamic ASCII bar graph
- Runs for 5 seconds by default

## Requirements
- Python 3.x
- sounddevice
- numpy

## Installation
Install the required Python packages:
```powershell
pip install sounddevice numpy
```

## Usage
Run the script:
```powershell
python Code.py
```
Speak or make sounds into your microphone and watch the bar graph change in real time.

## Notes
- Make sure your microphone is connected and accessible.
- You can adjust the duration by changing the value in `sd.sleep(5000)` (milliseconds).
- Works on Windows, macOS, and Linux (with compatible audio drivers).

## License
This project is provided for educational purposes.
