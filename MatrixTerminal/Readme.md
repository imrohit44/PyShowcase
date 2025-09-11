# MatrixTerminal

MatrixTerminal is a simple Python program that creates a "Matrix rain" effect in your terminal window. It continuously prints random symbols across the width of your terminal, simulating the iconic digital rain from the Matrix movies.

## Features
- Prints random characters and symbols in each row
- Adapts to your terminal's current width
- Runs continuously until stopped

## Requirements
- Python 3.x
- No external dependencies

## Usage
Run the script:
```powershell
python Code.py
```
Press `Ctrl+C` to stop the program.

## Notes
- Works on Windows, macOS, and Linux terminals that support `os.get_terminal_size()`.
- You can adjust the speed by changing the value in `time.sleep(0.05)` (seconds).
- For best effect, use a terminal with a black background and green text.

## License
This project is provided for educational purposes.
