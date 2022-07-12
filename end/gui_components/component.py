from base.dimensions import Dimensions
from base.important_variables import game_window
from base.utility_functions import *


class Component(Dimensions):
    color = None
    path_to_image = None

    def __init__(self, path_to_image=""):
        self.path_to_image = path_to_image

        if path_to_image != "":
            load_image(path_to_image)

    def run(self):
        pass

    def render(self):
        if self.path_to_image != "":
            render_image(self.path_to_image, self.left_edge, self.top_edge, self.length, self.height)

        else:
            render_rectangle(self.left_edge, self.top_edge, self.length, self.height, self.color)

    def got_clicked(self):
        return mouse_is_clicked() and is_mouse_collision(self)