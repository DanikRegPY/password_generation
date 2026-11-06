import secrets
import string
from unittest import result


def gen_pass(length=12, use_digits=True, use_symbols=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    password = "".join(secrets.choice(chars) for _ in range(length))
    return password


def get_length():
    while True:
        try:
            length = int(input("Введите длину пароля: "))
        except ValueError:
            print("Нужно ввести число, например 12")
            continue
        if length < 4:
            print("Слишком коротко, минимум 4 символа")
            continue
        return length


def ask_yes_no(question):
    while True:
        answer = input(question).lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
    print("Нужно ввести y или n")


def main():
    length = get_length()
    digits = ask_yes_no("Использовать цифры (y/n): ")
    symbols = ask_yes_no("Использовать символы (y/n): ")
    print("Сгенерированный пaроль: ", gen_pass(length, digits, symbols))


if __name__ == "__main__":
    main()