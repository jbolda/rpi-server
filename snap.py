import sys

import hitherdither
from inky import auto
from PIL import Image


def draw_snapshot():
    saturation = 0.75

    palette = hitherdither.palette.Palette(
        inky._palette_blend(saturation, dtype='uint24'))

    image = Image.open('./snapshot.jpg').convert("RGB")
    image_resized = image.resize(inky.resolution)

    # VERY slow (1m 40s on a Pi 4) - see https://github.com/hbldh/hitherdither for a list of methods
    # image_dithered = hitherdither.diffusion.error_diffusion_dithering(image_resized, palette, method="stucki", order=2)

    # Usably quick, your vanilla dithering
    image_dithered = hitherdither.ordered.bayer.bayer_dithering(
        image_resized, palette, thresholds, order=8)

    # Usuably quick, half-tone comic-book feel, use order=4 for small dots and order=8 dot bigguns
    # image_dithered = hitherdither.ordered.cluster.cluster_dot_dithering(image_resized, palette, thresholds, order=8)

    # VERY slow
    # image_dithered = hitherdither.ordered.yliluoma.yliluomas_1_ordered_dithering(image_resized, palette, order=8)

    inky.set_image(image_dithered.convert("P"))
    inky.show()
