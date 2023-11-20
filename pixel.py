from typing import List


class Pixel:
    x: int              # x coord
    y: int              # y coord
    red: int            # red value
    green: int          # green value
    blue: int           # blue value
    checked: bool = False       # if pixel has been previously checked

    def __init__(self, x: int, y: int, r: int, g: int, b: int):
        self.x = x
        self.y = y
        self.red = r
        self.green = g
        self.blue = b

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f"y: {self.y} x: {self.x} \nRed   : {self.red}\nGreen : {self.green}\nBlue  : {self.blue}\n"

    def __repr__(self):
        return f"Pixel(y: {self.y} x: {self.x} \nRed   : {self.red}\nGreen : {self.green}\nBlue  : {self.blue}\n)"

    def same_colour(self, other) -> bool:
        return (self.red == other.red) and (self.green == other.green) and (self.blue == other.blue)

    def get_colour_as_list(self):
        return [self.red, self.green, self.blue]

    def set_colour(self, colour: List[int]):
        self.red = colour[0]
        self.green = colour[1]
        self.blue = colour[2]
