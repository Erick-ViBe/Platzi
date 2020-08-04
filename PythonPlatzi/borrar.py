def run():
    f = int(raw_input())
    g = int(raw_input())

    x = []
    for i in range(f):
        x.append([])
        for j in range(g):
            aux = int(raw_input())
            x[i].append(factorial(aux))

    for t in range(f):
        for y in range(g):
            print(x[t][y]),
        print('')

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)


if __name__ == '__main__':
    run()
