from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.widget import Widget


class BackgroundWidget(Widget):
    pass


class DrawWidget(Widget):
    rect_size = (10, 10)
    rect_pos = (0, 0)
    color = [0, 0, 0, 1]

    def on_touch_down(self, touch):
        self.rect_pos = touch.pos
        with self.canvas:
            Color(self.color[0], self.color[1], self.color[2], self.color[3], mode="rgba")
            Rectangle(pos=touch.pos, size=self.rect_size)

    def on_touch_move(self, touch):
        self.rect_pos = touch.pos
        with self.canvas:
            Color(self.color[0], self.color[1], self.color[2], self.color[3], mode="rgba")
            Rectangle(pos=touch.pos, size=self.rect_size)

    def change_color(self, r, g, b, a):
        self.color[0] = int(r) % 255
        self.color[1] = int(g) % 255
        self.color[2] = int(b) % 255
        self.color[3] = float(a)
        print(self.color)

    def change_size(self, size):
        self.rect_size = (int(size), int(size))
        print(self.rect_size)
