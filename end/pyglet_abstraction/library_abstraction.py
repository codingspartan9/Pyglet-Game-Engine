import pyglet

mouse_position = []
window = pyglet.window.Window(0, 0, "title")

background_color = None
background_filler = None

keys = pyglet.window.key.KeyStateHandler()
mouse_buttons = pyglet.window.mouse.MouseStateHandler()
