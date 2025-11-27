"""Contains main controller and main function"""

import asyncio
import os
from enum import Enum
from typing import List

from server import Server

PERSON = [" O ", "/|\\", "/ \\"]

# suitable for a vscode terminal under the text editor.
# if you are using independent panel, 80, 40 may be suitable.
WIDTH, HEIGHT = 40, 10


class Direction(Enum):
    """Direction enum class"""

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class ScreenDisplay:
    """Controller used to manage screen"""

    def __init__(
        self, width: int, height: int, person: List[str], with_boarder: bool = False
    ):
        self._width = width
        self._height = height
        # the index of left-upper corner of person
        # 0 <= x < width - person_width + 1, y similar
        self._x = 0
        self._y = 0
        self._person = person
        self._person_width = len(person[0])
        self._person_height = len(person)
        self._boarder = with_boarder

    def move(self, direction: Direction) -> None:
        """change the position of person using given direction"""
        if direction == Direction.DOWN:
            self._y += 1 if self._y < self._height - self._person_height else 0
        elif direction == Direction.UP:
            self._y -= 1 if self._y > 0 else 0
        elif direction == Direction.LEFT:
            self._x -= 1 if self._x > 0 else 0
        elif direction == Direction.RIGHT:
            self._x += 1 if self._x < self._width - self._person_width else 0
        else:
            pass

    def draw(self):
        """refresh the screen and draw the cute ascii person"""
        os.system("clear")
        print(str(self))

    def __str__(self):
        result = ""
        if self._boarder:
            result += "-" * (self._width + 2) + "\n"
        for i in range(self._height):
            line = " " * self._width
            if i in range(self._y, self._y + self._person_height):
                line = (
                    line[: self._x]
                    + self._person[i - self._y]
                    + line[self._x + self._person_width :]
                )
            result += "|" + line + "|\n" if self._boarder else line
        if self._boarder:
            result += "-" * (self._width + 2) + "\n"
        return result


async def main():
    """The main function"""
    screen = ScreenDisplay(WIDTH, HEIGHT, PERSON, True)
    screen.draw()

    server = Server("127.0.0.1", 1999)
    server.bind_screen(screen)

    await server.serve_forever()


asyncio.run(main())
