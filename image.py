import sys

from PIL import Image

from inky.auto import auto

inky = auto(ask_user=True, verbose=True)


def draw_image():
    saturation = 0.5
    image = Image.open("screenshot.jpg")
    resizedimage = image.resize(inky.resolution)

    if len(sys.argv) > 2:
        saturation = float(sys.argv[2])

    inky.set_image(resizedimage, saturation=saturation)
    inky.show()
