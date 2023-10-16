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


def mysum(llist=[]):
    sum = 0
    for n in llist:
        sum += n
    return sum


def standard(arg):
    print(arg)


def positional_only(pos, /):
    print(pos)


def keyword_only(*, keyword):
    print(keyword)


def all(pos, /, combined, *, keyword):
    print(pos, combined, keyword)


def mysum2(*values):
    print(type(values), values)
    sum = 0
    for n in values:
        sum += n
    return sum


fib()
fib(100)
fib(1000)
print(fib)
print(fib(200))
print(fib2())
fib2(200)
data = fib2(20)
print(data)
print(fib2)
print(fib2(20))

print(mysum([1, 2, 3, 4, 5]))
print(mysum())

standard(22)  # positional argument
standard(arg=11)  # keyword argument

positional_only(33)
# positional_only(pos=44)

keyword_only(keyword=44)
# keyword_only(55)

all(100, 200, keyword=300)
all(1000, combined=2000, keyword=3000)

print(mysum2(1, 2, 3))
print(mysum2(11, 22, 33, 44, 55))

numbers = []
for i in range(3):
    numbers.append(int(input('n= ')))
print(type(numbers), numbers)

numbers = list(map(int, input('list: ').split()))
print(type(numbers), numbers)

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(sum(numbers))
