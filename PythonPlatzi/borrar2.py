# -*- coding: utf-8 -*-

def run ():
    x = int(raw_input())
    y = int(raw_input())

    result = power(x, y)

    print result


def power(x, y):
    return x**y


if __name__ == '__main__':
    run()
