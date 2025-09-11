import winsound

def text_to_beeps(text):
    for ch in text:
        freq = 200 + (ord(ch) % 2000)   # Frequency based on character
        winsound.Beep(freq, 150)        # Beep for 150ms

if __name__ == "__main__":
    text = "HELLO"
    text_to_beeps(text)
