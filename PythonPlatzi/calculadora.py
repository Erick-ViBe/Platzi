# -*- coding: utf-8 -*-

def run():
    print('***** C A L C U L A D O R A *****')
    print('')

    n1 = float(raw_input('Primer Numero: '))
    n2 = float(raw_input('Segundo Numero: '))

    print('')
    print('1---------------Suma')
    print('2--------------Resta')
    print('3-----Multiplicacion')
    print('4-----------Division')

    desicion = int(raw_input('Que operacion desea hacer: '))

    if desicion == 1:
        print('El resultado es: {}'.format(suma(n1, n2)))
    elif desicion == 2:
        print('El resultado es: {}'.format(resta(n1, n2)))
    elif desicion == 3:
        print('El resultado es: {}'.format(multiplicacion(n1, n2)))
    elif desicion == 4:
        print('El resultado es: {}'.format(division(n1, n2)))

def suma(n1, n2):
    return n1+n2

def resta(n1, n2):
    return n1-n2

def multiplicacion(n1, n2):
    return n1*n2

def division(n1, n2):
    return n1/n2

if __name__ == '__main__':
    run()
