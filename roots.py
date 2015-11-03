def sqrt(x):
    """ Compute square roots using method of Heron of Alexndria.

    Args:
        x: The number of which the square root is to be computed.

    Returns:
        The square root fo x.
    """
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ZeroDivisionError:
        print("Cannot compute square root of a negative number.")


if __name__ == '__main__':
    main()