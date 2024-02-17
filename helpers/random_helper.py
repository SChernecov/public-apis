import random

punctuations = r"""!"#$%&'()*+,-—–./:;<=>?@[\]^_`{|}~№«»“”„‹›‘’‚"""
whitespaces = ' \t\n\r\v\f'


def random_punctuations():
    """Generate random punctuations"""

    return ''.join(random.choice(punctuations) for _ in range(10))


def random_whitespaces():
    """Generate random whitespaces"""

    return ''.join(random.choice(whitespaces) for _ in range(10))


def random_bool():
    """Generate random bool param"""

    return random.choice([True, False])


def random_int():
    """Generate random number between 1 and 100"""

    return random.randint(1, 100)
