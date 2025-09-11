# ToneType

ToneType is a simple Python program that converts text into a sequence of beeps using the Windows `winsound` library. Each character in the input text is mapped to a unique beep frequency, allowing you to "hear" the text as tones.

## Features
- Converts any text string into a series of beeps
- Frequency of each beep is based on the character's Unicode value
- Runs on Windows using the built-in `winsound` module

## Requirements
- Python 3.x (Windows only)
- No external dependencies

## Usage
1. Open `Code.py` and modify the `text` variable to your desired string:
   ```python
   text = "HELLO"
   text_to_beeps(text)
   ```
2. Run the script:
   ```powershell
   python Code.py
   ```
   You will hear a series of beeps corresponding to each character in the text.

## Notes
- This program only works on Windows, as it uses the `winsound` module.
- Each character produces a beep with a frequency between 200 Hz and 2200 Hz for 150 milliseconds.

## License
This project is provided for educational purposes.
