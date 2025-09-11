import random, time, os
symbols = "01abcdefghijklmnopqrstuvwxyz#$%&@"
columns = os.get_terminal_size().columns

while True:
    print("".join(random.choice(symbols + "  ") for _ in range(columns)))
    time.sleep(0.05)
