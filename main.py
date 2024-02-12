from core.window import Window
from core.engine import Engine
from core.logic import ApplicationLogicInterface

import pygame


class MyLogic(ApplicationLogicInterface):
    def __init__(self):
        self.mouse_click = (0, 0)
    
    def input(self, window: Window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_click = pygame.mouse.get_pos()
    
    def update(self, window: Window):
        ...
    
    def render(self, window: Window):
        screen = window.screen

        background_color = (255, 0, 255)
        screen.fill(background_color)

        pygame.draw.rect(screen, (0, 255, 0), (*self.mouse_click, 5, 5))

        pygame.display.update()


window = Window("Window", 400, 400)
logic = MyLogic()
engine = Engine(window, logic)
engine.run()
