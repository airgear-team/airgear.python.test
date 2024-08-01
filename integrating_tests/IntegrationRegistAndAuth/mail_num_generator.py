import random
import string


class Generator:

    @staticmethod
    def generate_mail(length: int = 10, domain: string = 'test.test') -> string:
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return f"{random_string}@{domain}"

    @staticmethod
    def generate_num(code: string = "+380"):
        remaining_digits = random.randint(100000000, 999999999)
        return f"{code}{remaining_digits}"


def main():
    pass


if __name__ == "__main__":
    main()
