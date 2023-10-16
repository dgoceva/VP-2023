import datetime

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
for n in numbers:
    print(n, end=' ')
print()

print(len(numbers))
for i in range(len(numbers)):
    print(numbers[i], end=' ')
print()

for i in range(len(numbers)):
    numbers[i] *= 5

print(numbers)

for i in numbers:
    i *= 100
print(numbers)

even = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
print(even)

print(even[-1])
even[-1] = 121
print(even)
numbers[2:4] = [111, 222, 333, 444]
print(numbers)

a, b = 0, 1
while a < 10:
    print(a, end=' ')
    a, b = b, a+b
print()

fib = []
a, b = 0, 1
for i in range(10):
    fib.append(a)
    a, b = b, a+b
print(fib)

# dd-mm-yyyy
bdate = datetime.datetime.strptime(input('bdate= '), '%d-%m-%Y')
print(datetime.datetime.strftime(bdate+datetime.timedelta(days=100), '%d-%m-%Y'))

a, b = 0, 1
while a < 100:
    print(a, end=' ')
    a, b = b, a+b
print()

a, b = 0, 1
while a < 1000:
    print(a, end=' ')
    a, b = b, a+b
print()
