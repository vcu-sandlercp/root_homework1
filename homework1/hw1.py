""" This set of functions should return the appropriate data type"""


def return_number_3():
    """ This function should return an integer with the value of 3"""

    return_number_3 = 3
    return return_number_3


def return_string_vcu():
    """ This function should return a string with the lowercase value of vcu"""

    return_value = "vcu"
    return return_value


def return_lowercased_string(input_string):
    """You have a variable called input_string that is of type string.
    Return it but the lowercase version of it."""

    return_value = input_string
    return return_value.lower


def return_without_starting_ending_whitespace(input_string):
    """You have a variable called input_string that is of type string.
    Return it but with the surrounding (left and right) whitespace stripped."""

     input_string = "   testing string with whitespace   "
    return input_string.strip


def return_addition(first_number, second_number):
    """ Return the two numbers added together. """
    first_number = 1
    second_number = 2
    return_value = first_number + second_number
    return return_value
