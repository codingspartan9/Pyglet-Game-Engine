from math import sqrt

from base.fraction import Fraction
from base.important_variables import keyboard, game_window, SCREEN_LENGTH, SCREEN_HEIGHT
import random

from library_abstraction.utility_functions import *
from base.range import Range


def key_is_pressed(key):
    """:returns: bool; whether that key is currently held down (pressed)"""

    return keyboard.get_key_event(key).happened_this_cycle


def key_is_clicked(key):
    """:returns: bool; whether the key was not held down last cycle and is this cycle (clicked)"""

    return keyboard.get_key_event(key).is_click()


def key_has_been_released(key):
    """:returns: bool; whether the key was held down last cycle and is not this cycle (released)"""
    return keyboard.get_key_event(key).has_stopped()


def get_time_of_key_being_held_in(key):
    """:returns: float; the amount of time that the key has been held down"""

    return keyboard.get_key_timed_event(key).current_time


def mouse_is_clicked():
    """:returns: bool; whether the mouse was not pressed last cycle and is this cycle (clicked)"""

    return keyboard.mouse_clicked_event.is_click()


def get_index_of_range(number, range_lengths=[], ranges=None):
    """ Finds the index of the range that contains the current number. A range is defined by the numbers between
        two adjacent indexes (range_lengths[0] -> range_lengths[1])

        :parameter range_lengths: float[]; the lengths of the ranges. For instance, if the range_lengths is [1, 1, 1] then the ranges would be [0 -> 1, 1 -> 2, 2 -> 3]
        :parameter number: float; the number that is wanted to be within a range

        :returns: int; The index of the range that contains the number and -1 no range contains it"""

    index = -1

    if ranges is None:
        ranges = get_ranges(range_lengths)

    for x in range(len(ranges)):
        if ranges[x].__contains__(number):
            index = x
            break

    return index

def get_ranges(range_lengths):
    """:returns: Range[]; the ranges gotten from the range_lengths. A range is defined by two adjacent indexes (range_lengths[0] -> range_lengths[1])"""

    return_value = []
    current_value = 0

    for range_length in range_lengths:
        return_value.append(Range(current_value, current_value + range_length))
        current_value += range_length

    return return_value

def is_within_screen(game_object):
    """:returns: bool; if the game_object is within the screen (can be seen on the screen)"""

    return (game_object.right_edge > 0 and game_object.left_edge < SCREEN_LENGTH and
            game_object.bottom_edge > 0 and game_object.top_edge < SCREEN_HEIGHT)


def is_random_chance(probability: Fraction):
    """ Uses the probability for the random chance (for instance if the probability is 7/10 then 7 out of 10
        times it will return True and the other 3 times it will return False)

        :parameter probability: Fraction; the probability this function will return True

        :returns: bool; if the random number between 1-probability.denominator is >= probability.numerator
    """

    return random.randint(1, probability.denominator) <= probability.numerator


def is_beyond_screen_left(left_edge):
    """:returns: bool; if the left_edge is beyond the left side of the screen"""

    return left_edge <= 0


def is_beyond_screen_right(right_edge):
    """:returns: bool; if the right_edge is beyond the right side of the screen"""

    return right_edge >= SCREEN_LENGTH


def min_value(item1, item2):
    """:returns: float; the smallest item"""

    if item1 is None:
        return item2

    if item2 is None:
        return item1

    return item1 if item1 < item2 else item2


def max_value(item1, item2):
    """returns float; the biggest item"""

    return item1 if item1 > item2 else item2


def get_combined_number_values(numbers):
    """:returns: float or int; all the numbers in 'numbers' added up together in one number"""

    return_value = 0

    for number in numbers:
        return_value += number

    return return_value

def get_next_index(current_index, max_index):
    """:returns: int; the index after current_index (it cycles, so once it gets beyond the max_index it goes back to 0)"""

    next_index = current_index + 1
    return next_index if next_index <= max_index else 0


def get_previous_index(current_index, max_index):
    """:returns: int; the index before current_index (it cycles, so once it gets below 0 it goes to the max_index"""

    prev_index = current_index - 1
    return prev_index if prev_index >= 0 else max_index

def rounded(number, places):
    """:returns: float; the number rounded to that many decimal places"""

    rounded_number = int(number * pow(10, places))

    # Converting it back to the proper decimals once it gets rounded from above
    return rounded_number / pow(10, places)

def get_kwarg_item(kwargs, key, default_value):
    """ :parameter kwargs: dict; the **kwargs
        :parameter key: Object; the key for the item
        :parameter default_value: Object; the value that will be obtained if the kwargs doesn't contain the key

        :returns: Object; kwargs.get(key) if kwargs contains the key otherwise it will return the default_value
    """

    return kwargs.get(key) if kwargs.__contains__(key) else default_value

def solve_quadratic(a, b, c):
    """:returns: float[]; [answer1, answer2] the answers to the quadratic
                and if the answer is an imaginary number it returns float('nan')"""

    number_under_square_root = pow(b, 2) - 4 * a * c
    number_under_square_root = rounded(number_under_square_root, 4)

    if number_under_square_root < 0:
        return None

    square_root = sqrt(number_under_square_root)

    answer1 = (-b + square_root) / (2 * a)
    answer2 = (-b - square_root) / (2 * a)

    answers = [answer2, answer1]

    # If the answers are the same I should only return one of them
    return answers if answers[0] != answers[1] else [answers[0]]