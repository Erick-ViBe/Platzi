# -*- coding: utf-8 -*-

def run():
    counter = 0
    with open('cuento.txt') as f:
        for line in f:
            counter += line.count('toro')

    print('La palabra toro se encuentra {} veces en el texto'.format(counter))

if __name__ == '__main__':
    run()
