# -*- coding: utf-8 -*-

from lamp import Lamp


def run():
    lamp = Lamp(is_turned_on=False)

    while True:
        command = str(raw_input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [m]ostrar
            [s]alir
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        elif command == 'm':
            lamp._display_image()
        else:
            break


if __name__ == '__main__':
    run()
