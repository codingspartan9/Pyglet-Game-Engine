import time
from base.important_variables import *
from base.history_keeper import HistoryKeeper
from base.velocity_calculator import VelocityCalculator
from pyglet_library.utility_functions import *

def run_game(main_screen):
    game_window.add_screen(main_screen)
    call_every_cycle(_run_game_every_cycle)


def _run_game_every_cycle(cycle_time, is_start_time):
    keyboard.run()
    game_window.run()

    if is_start_time:
        cycle_time = time.time() - cycle_time

    HistoryKeeper.last_time = VelocityCalculator.time
    VelocityCalculator.time = cycle_time



