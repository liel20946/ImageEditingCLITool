
def check_two_positive_ints(*args):
    """
    Check that the arguments are two positive integers.
    :param args: the arguments to check.
    :return: True if the arguments are two positive integers, False otherwise.
    """
    if len(args) != 2:
        return False
    return (args[0].isdigit() and args[1].isdigit()
            and int(args[0]) > 0 and int(args[1]) > 0)


def check_non_negative_float(*args):
    """
    Check that the argument is a float.
    :param args: the arguments to check.
    :return: True if the argument is a float, False otherwise.
    """
    if len(args) != 1:
        return False
    return args[0].replace('.', '', 1).isdigit()


def check_one_float(*args):
    """
    Check that the argument is a float.
    :param args: the arguments to check.
    :return: True if the argument is a float, False otherwise.
    """
    if len(args) != 1:
        return False
    float_str = args[0]
    if args[0].startswith('-'):
        float_str = args[0][1:]
    return float_str.replace('.', '', 1).isdigit()

