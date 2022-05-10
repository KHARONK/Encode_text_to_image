from re import I
from PIL import Image
from helpers import data_to_binary, encode_text_to_image

IMAGE_NAME = "./dog.png"
ENCODED_IMAGE_NAME = "encoded.png"

def encode_image():
    """Encode image"""
    # Taking user input
    phrase = input("Enter a word to encode: \n\n")

    # Convert input to binary format.
    binary_phrase = data_to_binary(phrase)

    # Read image.
    with Image.open(IMAGE_NAME) as image:

        # get image byte so that tou can compare with that of message to encode
        image_byte = (image.size[0] * image.size[1] * 3) // 8

        # Compare size of converted text to binary to the images'.
        if len(binary_phrase) > image_byte:
            raise ValueError("please use a larger image")

        # Make copy of image to avoid mutation of the images' original pixels.
        image_copy = image.copy()
        encode_text_to_image(image_copy, binary_phrase)

        # save new encoded image
        image_copy.save(ENCODED_IMAGE_NAME, "png")


def decode_image():
    with Image.open(ENCODED_IMAGE_NAME) as image:

        data = ''
        # iter util function to iterate the data.
        image_data = iter(image.getdata())

        while True:
            # RGB values conversion to bits.
            pixels = [value for value in image_data.__next__()[:3] +
                      image_data.__next__()[:3] +
                      image_data.__next__()[:3]]

            # Bits concatenation into string from User.
            binstr = ''
            for i in pixels[:8]:
                if (i % 2 == 0):
                    binstr += '0'
                else:
                    binstr += '1'

            data += chr(int(binstr, 2))
            if (pixels[-1] % 2 != 0):
                return data


def get_user_input():
    # Mode options for User.
    selected_mode = input("Please choose a mode: \n1. encode image\n2. decode image\nq. Press to quit\n\n")

    if selected_mode == "1":
        encode_image()
    elif selected_mode == "2":
        print(f"decoded text: {decode_image()}")
    elif selected_mode.lower() == "q":
        print("quitting")
        quit(1)


if __name__ == '__main__':
    get_user_input()