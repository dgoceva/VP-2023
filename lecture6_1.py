def fib(limit=10):
    a, b = 0, 1
    while a < limit:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(upper=10):
    result = []
    a, b = 0, 1
    for i in range(upper):
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == '__main__':
    print('Test')
    import sys
    print(sys.argv)
    if len(sys.argv) > 1 and sys.argv[1] != '':
        fib(int(sys.argv[1]))
    else:
        fib()
