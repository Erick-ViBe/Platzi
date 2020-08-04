# -*- coding: utf-8 -*-

def run():
    print('***** S U M A   R E C U R S I V A *****')
    print('')

    number = int(raw_input('Ingresa numero: '))

    r = recursive_sum(number)

    print('')
    print('El resultado es: {}'.format(r))


def recursive_sum(number):
    if number == 1:
        return 1
    else:
        return number + recursive_sum(number-1)


if __name__ == '__main__':
    run()
