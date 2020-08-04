# -*- coding: utf-8 -*-

def run():
    char_sequence = str(raw_input('Escribe una secuencia de caracteres: '))

    result = repeating_chars(char_sequence)

    if result:
        for i in range(len(result)):
            print('La letra {} se repite {} veces'.format(result[i][0], result[i][1]))
    else:
        print('Ninguna letra se repite')

def repeating_chars(char_sequence):
    seen_letters = {}

    for idx, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (idx, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letters = []

    for key, value in seen_letters.iteritems():
        if value[1] > 1:
            final_letters.append((key, value[1]))

    repeated_letters = sorted(final_letters, key=lambda value: value[1])

    return repeated_letters

if __name__ == '__main__':
    run()
