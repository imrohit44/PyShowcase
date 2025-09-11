# ImageSteganographer

ImageSteganographer is a Python program that hides a secret message inside an image using simple steganography. It modifies the least significant bit (LSB) of the red channel of each pixel to encode the message in binary form.

## Features
- Encodes a text message into an image file
- Uses LSB steganography on the red channel
- Outputs a new image with the hidden message

## Requirements
- Python 3.x
- Pillow (PIL)

## Installation
Install the required Python package:
```powershell
pip install pillow
```

## Usage
1. Place your input image (e.g., `input.png`) in the program directory.
2. Edit the script to set your message and output filename:
   ```python
   encode("input.png", "SECRET MESSAGE", "encoded.png")
   ```
3. Run the script:
   ```powershell
   python Code.py
   ```
4. The encoded image will be saved as `encoded.png`.

## Notes
- Only the first N pixels (where N is the number of bits in your message) are modified.
- The image must be large enough to hold the entire message (8 pixels per character).
- This script only encodes messages; it does not decode them.

## License
This project is provided for educational purposes.
