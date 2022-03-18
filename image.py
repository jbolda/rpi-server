import sys

from PIL import Image

from inky.auto import auto


def draw_image():
    inky = auto(ask_user=True, verbose=True)
    saturation = 0.5
    image = Image.open("./screenshot.jpg")
    resizedimage = image.resize(inky.resolution)

    if len(sys.argv) > 2:
        saturation = float(sys.argv[2])

    inky.set_image(resizedimage, saturation=saturation)
    inky.show()
