from core.window import Window
from core.logic import ApplicationLogicInterface


class Engine:
    __window: Window
    __logic: ApplicationLogicInterface

    def __init__(self, window: Window, logic: ApplicationLogicInterface):
        self.__window = window
        self.__logic = logic

    def run(self):
        while True:
            self.__logic.input(self.__window)
            self.__logic.update(self.__window)
            self.__logic.render(self.__window)