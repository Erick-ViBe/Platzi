# -*- coding: utf-8 -*-
import random

def run():
    number_found = False
    max = int(raw_input('Hasta que numero quieres adivinar: '))
    random_number = random.randint(0, max)

    while not number_found:
        number = int(raw_input('Intenta un numero: '))

        if number == random_number:
            print('Felicidades!!!. Encontraste el numero')
            number_found = True
        elif number > random_number:
            print('El numero es menor')
        else:
            print('El numero es mas grande')


if __name__ == '__main__':
    run()
