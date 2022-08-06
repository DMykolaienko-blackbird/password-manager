import random

LETTERS_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
SPECIAL_CHARS_LIST = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+"]



class Password:

    def __init__(self, lower_letters_count, upper_letters_count, special_chars_count, numbers_count):
        self._lower_letters_count = lower_letters_count
        self._upper_letters_count = upper_letters_count
        self._special_chars_count = special_chars_count
        self._numbers_count = numbers_count

    def generate_password(self):
        generated_list = self.get_random_lower_combination() + \
                         self.get_random_upper_combination() + \
                         self.get_random_special_chars_combination() + \
                         self.get_random_numbers_combination()
        random.shuffle(generated_list)
        return "".join(generated_list)

    def set_lower_letters_count(self, lower_letters_count):
        self._lower_letters_count = lower_letters_count

    def set_upper_letters_count(self, upper_letters_count):
        self._upper_letters_count = upper_letters_count

    def set_special_chars_count(self, special_chars_count):
        self._special_chars_count = special_chars_count

    def get_random_lower_combination(self):
        random_list = [random.choice(LETTERS_LIST) for _ in range(self._lower_letters_count)]
        return random_list

    def get_random_upper_combination(self):
        random_list = [random.choice(LETTERS_LIST).upper() for _ in range(self._upper_letters_count)]
        return random_list

    def get_random_special_chars_combination(self):
        random_list = [random.choice(SPECIAL_CHARS_LIST) for _ in range(self._special_chars_count)]
        return random_list

    def get_random_numbers_combination(self):
        random_list = [str(random.randint(0, 9)) for _ in range(self._numbers_count)]
        return random_list

