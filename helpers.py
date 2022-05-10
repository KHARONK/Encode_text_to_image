def data_to_binary(data):
    """convert data to binary format"""
    if type(data) == str:
        return [format(ord(i), "08b") for i in data]
    if type(data) == bytes:
        return [format(i, "08b") for i in data]
    if type(data) == int:
        return format(data, "08b")
    return None

# generate_data function using pixels with text to encode.
# Pixels conversion to 8 bit binary.
def generate_data(pixels, binary_data):
    length_of_data = len(binary_data)
    image_data = iter(pixels)

    for i in range(length_of_data):
        # Extracting 3 pixels at a time
        pixels = [value for value in image_data.__next__()[:3] +
                  image_data.__next__()[:3] +
                  image_data.__next__()[:3]]

        for j in range(0, 8):
            # Comparing RGB values to binary data.
            if (binary_data[i][j] == '0' and pixels[j] % 2 != 0):
                pixels[j] -= 1

            elif (binary_data[i][j] == '1' and pixels[j] % 2 == 0):
                if (pixels[j] != 0):
                    pixels[j] -= 1
                else:
                    pixels[j] += 1

        if (i == length_of_data - 1):
            if (pixels[-1] % 2 == 0):
                if (pixels[-1] != 0):
                    pixels[-1] -= 1
                else:
                    pixels[-1] += 1

        else:
            if (pixels[-1] % 2 != 0):
                pixels[-1] -= 1

        pixels = tuple(pixels)
        yield pixels[:3]
        yield pixels[3:6]
        yield pixels[6:9]


def encode_text_to_image(image, binary_data):
    # This method will encode data to the new image that will be created

    image_width = image.size[0]
    (x, y) = (0, 0)

    converted_pixels = generate_data(image.getdata(), binary_data)

    for pixel in converted_pixels:

        image.putpixel((x, y), pixel)
        if (x == image_width - 1):
            x = 0
            y += 1
        else:
            x += 1

