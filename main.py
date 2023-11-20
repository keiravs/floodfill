from PIL import Image
import numpy
from pixel import Pixel
from typing import List
import matplotlib.pyplot as plt

RED = 0
GREEN = 1
BLUE = 2

PURPLE = [157, 66, 137]


def create_pixel_list(array: numpy.ndarray) -> List[List[Pixel]]:
    array = list(array)
    output_array: List[List[Pixel]] = []

    for rowindex, row in enumerate(array):
        current_row = []
        for colindex, pixel in enumerate(row):
            current_row.append(Pixel(x=colindex, y=rowindex, r=pixel[RED], g=pixel[GREEN], b=pixel[BLUE]))
        output_array.append(current_row)
    return output_array


def create_colour_list(pixels: List[List[Pixel]]) -> List[List[int]]:
    output = []
    r = 0
    c = 0
    for row in pixels:
        cur_row = []
        for pixel in row:
            cur_row.append(pixel.get_colour_as_list())
        output.append(cur_row)
    return output

# TODO: IMPLEMENT move()
# Moves in a given direction in the image
def move(direction: str, cur_pixel: Pixel, image: List[List[Pixel]]) -> Pixel or None:
    pass


# TODO: IMPLEMENT search()
# Searches image for all reachable areas from starting coordinates x, y.
def search(x: int, y: int, image: List[List[Pixel]]) -> List[List[Pixel]]:
    pass


def write_image_from_array(array: numpy.array, outfile: str):
    width = len(array[0])
    height = len(array)
    out_image = Image.new("RGB", (width, height))

    for rowindex, row in enumerate(array):
        for columnindex, pixel in enumerate(row):
            out_image.putpixel((columnindex, rowindex), tuple(pixel))
    out_image.save(outfile)
    return out_image


def main():
    image = Image.open('images/terrain2.png')
    image_as_array = numpy.array(image)
    image_as_pixel_array = create_pixel_list(image_as_array)

    start_x = 181
    start_y = 211

    # Get new image array
    print("Searching...")
    output_image_pixel_array = search(start_x, start_y, image_as_pixel_array)

    print("Converting back to colour array...")
    # Convert array of pixels back to list of lists
    output_colour_array = create_colour_list(output_image_pixel_array)

    print("Writing new image to file...")
    im = write_image_from_array(numpy.array(output_colour_array), "images/output_image.png")
    f, axes = plt.subplots(1, 2)
    axes[0].imshow(image)
    axes[1].imshow(im)
    plt.show()
    print("Done!")


if __name__ == '__main__':
    main()
