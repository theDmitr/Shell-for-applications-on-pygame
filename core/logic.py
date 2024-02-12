from core.window import Window


class ApplicationLogicInterface:
    def input(self, window: Window):
        raise NotImplementedError
    
    def update(self, window: Window):
        raise NotImplementedError
    
    def render(self, window: Window):
        raise NotImplementedError
