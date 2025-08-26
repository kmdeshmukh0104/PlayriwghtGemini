import random
import string

class CommonFunctions:
    def random_string(length=10):
        characters = string.ascii_lowercase + string.digits
        return ''.join(random.choice(characters) for _ in range(length))