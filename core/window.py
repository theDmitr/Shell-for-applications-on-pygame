import pygame as pg


class Window:
    __screen: pg.Surface

    def __init__(self, title: str, width: int, height: int, flags: int = 0, depth: int = 0, display: int = 0, vsync: int = 0):
        self.__screen = pg.display.set_mode(size=(width, height), flags=flags, depth=depth, display=display, vsync=vsync)
        pg.display.set_caption(title)

    @property
    def screen(self):
        return self.__screen
