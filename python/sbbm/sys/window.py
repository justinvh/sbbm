import pyglet


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        @self.event
        def on_draw():
            self.clear_frame()
            self.on_draw()

        @self.event
        def on_mouse_press(x, y, button, modifiers):
            pass

    def clear_frame(self):
        self.clear()

    def on_draw(self):
        pass
