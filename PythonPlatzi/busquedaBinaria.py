# -*- coding: utf-8 -*-

def run():
    list_of_numbers = [2, 5, 8, 1, 6, 9, 3, 10, 4, 7]

    number = int(raw_input('Numero a buscar: '))

    result = binary_search(list_of_numbers, number)

    if result is True:
        print('Si esta en la lista')
    else:
        print('No esta en la lista')


def binary_search(list_of_numbers, number):
    list_of_numbers.sort()

    pivot = len(list_of_numbers)/2

    if list_of_numbers[pivot] == number:
        return True
    elif list_of_numbers > number:
        return binary_search(list_of_numbers[:pivot], number)
    elif list_of_numbers < number:
        return binary_search(list_of_numbers[pivot+1:], number)
    else:
        return False


if __name__ == '__main__':
    run()
