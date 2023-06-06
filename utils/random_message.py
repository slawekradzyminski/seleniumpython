import random
import string


def generate_random_text(length):
    result_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    return result_str
