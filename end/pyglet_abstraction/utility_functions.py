from pyglet.window import mouse

from pyglet_library.keys import *
from pyglet_library import library_abstraction
import pyglet
from pyglet import window, clock

images = {}
drawable_images = {}
text_boxes = {}
rectangles = {}

def load_image(path_to_image):
    if images.get(path_to_image) is None:
        images[path_to_image] = pyglet.image.load(path_to_image)

def load_text(name, font_size, background_color, text_color):
    text_boxes[name] = pyglet.text.Label("", font_name="Freesansbold", font_size=font_size, color=list(text_color)+[255])

def get_dimensions_conversion(left_edge, top_edge, height):
    return [left_edge, library_abstraction.window.height - top_edge - height]

def render_text(left_edge, top_edge, text_color, background_color, text, font_size, is_centered, name):
    left_edge, top_edge = get_dimensions_conversion(left_edge, top_edge, 0)
    text_box: pyglet.text.Label = text_boxes.get(name)

    if text_box.x != left_edge or text_box.y != top_edge:
        text_box.x, text_box.y = left_edge, top_edge

    if text_box.text != text:
        text_box.text = text

    anchor_type = "center" if is_centered else ""
    if text_box.anchor_x != anchor_type:
        text_box.anchor_x, text_box.anchor_y = anchor_type, anchor_type

    text_box.draw()

def render_image(path_to_image, left_edge, top_edge, length, height):
    left_edge, top_edge = get_dimensions_conversion(left_edge, top_edge, height)
    image = images.get(path_to_image)

    name = f"{path_to_image}{length}{height}"

    if drawable_images.get(name) is None:
        drawable_image = pyglet.sprite.Sprite(image, left_edge, top_edge)
        drawable_image.scale_x = length / drawable_image.width
        drawable_image.scale_y = height / drawable_image.height
        drawable_images[name] = drawable_image

    drawable_image = drawable_images.get(name)
    if drawable_image.x != left_edge or drawable_image.y != top_edge:
        drawable_image.x, drawable_image.y = left_edge, top_edge

    drawable_image.draw()


def render_rectangle(left_edge, top_edge, length, height, color):
    left_edge, top_edge = get_dimensions_conversion(left_edge, top_edge, height)
    name = f"{left_edge}{top_edge}{length}{height}{color}"

    if rectangles.get(name) is None:
        rectangles[name] = pyglet.shapes.Rectangle(left_edge, top_edge, length, height, color=color)

    rectangles.get(name).draw()

def set_up_window(length, height, background_color, title):
    library_abstraction.window.set_size(length, height)
    library_abstraction.window.set_caption(title)

    library_abstraction.background_color = background_color
    library_abstraction.background_filler = pyglet.shapes.Rectangle(0, 0, length, height, color=background_color)

    library_abstraction.window.push_handlers(library_abstraction.keys)
    library_abstraction.window.push_handlers(library_abstraction.mouse_buttons)

def key_is_pressed(keyboard_key):
    game_engine_key = keyboard_keys_to_game_engine_keys.get(keyboard_key)
    return library_abstraction.keys[game_engine_key]

def call_every_cycle(function):
    clock.schedule_interval(lambda time: _call_every_cycle(time, function), 1 / 120)
    pyglet.app.run()

def _call_every_cycle(time, function):
    library_abstraction.background_filler.draw()
    function(time, False)

def is_mouse_collision(dimensions):
    mouse_left_edge, mouse_top_edge = library_abstraction.mouse_position
    is_horizontal_collision = mouse_left_edge >= dimensions.left_edge and mouse_left_edge <= dimensions.right_edge
    is_vertical_collision = mouse_top_edge >= dimensions.top_edge and mouse_top_edge <= dimensions.bottom_edge
    return is_horizontal_collision and is_vertical_collision

def get_time_passed(unused):
    return -1

def get_mouse_position():
    return library_abstraction.mouse_position

@library_abstraction.window.event
def on_mouse_motion(x, y, dx, dy):
    library_abstraction.mouse_position = [x, y]

@library_abstraction.window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        return pyglet.event.EVENT_HANDLED

def mouse_was_pressed():
    return library_abstraction.mouse_buttons[pyglet.window.mouse.LEFT]
