from PIL import Image

def encode(img_path, message, output):
    img = Image.open(img_path)
    binary = ''.join(format(ord(i), '08b') for i in message)
    pixels = list(img.getdata())
    new_pixels = []
    
    for i in range(len(pixels)):
        if i < len(binary):
            pixel = list(pixels[i])
            pixel[0] = (pixel[0] & ~1) | int(binary[i])  # modify LSB
            new_pixels.append(tuple(pixel))
        else:
            new_pixels.append(pixels[i])
    img.putdata(new_pixels)
    img.save(output)

encode("input.png", "SECRET MESSAGE", "encoded.png")
