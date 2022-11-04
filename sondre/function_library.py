import random


def generate_list(range_from: int = 0, range_to: int = 100, length=20):
    """Generate a list filled with random integer values.
    Takes in variables starting range, end range and length of list. Values must be integers.
    If no input is given, range will default from 0 to 100, and length of list to 20 items."""

    generated_list = []
    for i in range(length):
        generated_list.append(random.randint(range_from, range_to))
    return generated_list
