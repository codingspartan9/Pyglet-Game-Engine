import time
from base.important_variables import *
from base.history_keeper import HistoryKeeper
from base.velocity_calculator import VelocityCalculator
from library_abstraction.utility_functions import *

def run_game(main_screen):
    """ Runs all the game code. This will add 'main_screen' to the 'game_window,' so the 'main_screen' components and run
        function can be called. If there should be multiple screens for this game, game_screen.add_screen() should be called.
        This function specifically calls game_window.add_screen() and call_every_cycle()"""

    game_window.add_screen(main_screen)
    call_every_cycle(_run_game_every_cycle)


def _run_game_every_cycle(cycle_time, is_start_time, should_render):
    """ Runs all the code that should be called every game cycle. This function updates all the game components. This
        function should generally not be called because the run_game method will do that for you"""

    keyboard.run()
    game_window.run(should_render)

    if is_start_time:
        cycle_time = time.time() - cycle_time

    HistoryKeeper.set_last_frame_id(VelocityCalculator.current_cycle_number)
    VelocityCalculator.time = cycle_time
    VelocityCalculator.current_cycle_number += 1



