# -*- coding: utf-8 -*-

def run():
    number = int(raw_input('Numero: '))
    result = factorial(number)
    print('El factorial es: {}'.format(result))


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)


if __name__ == '__main__':
    run()
