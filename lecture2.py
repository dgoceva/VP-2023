import random
import cmath
import math
import numpy as np

print(random.random())
print(random.randint(-10, 30))
print(random.randrange(1, 100))
print(random.uniform(-100, 99))

a = random.randint(-10, 10)
b = random.randint(-10, 10)
c = random.randint(-10, 10)
print(f'{a}x**2+{b}x+{c}=0')
print('{0}x**2+{1}x+{2}=0'.format(a, b, c))
if a == 0:
    print('No solution...')
else:
    d = b**2 - 4*a*c
    x1 = (-b-cmath.sqrt(d))/(2*a)
    x2 = (-b+cmath.sqrt(d))/(2*a)
    print('x1=', x1, '\nx2=', x2)
print('a=%.4f\tb=%.2f' % (a, b))
print(0.1+0.2)
print(round(0.1+0.2, 3))
print(math.ceil(0.1+0.2))
print(math.floor(0.1+0.2))

s = 'Hello, Python!'
print(s[0], s[5])
# print(s[30])
print(s[-1], s[-10])
print(s[:])
print(s[5:])
print(s[:10])
print(s[5:10])
print(s[:-10])
# s[1] = 'X'
print(s+'!!')
print(s+'3.14')
print(3*s)
print(cmath.sqrt.__doc__)
print(len(s))
print(s[len(s)-1])
print('python' in s)
print('Python' in s)
print('PYTHON' in s.upper())
print(s.islower())
print(s.isalpha())
print('C:\some\name')
print(r'C:\some\name')
print(s.index('P'))
if 'p' in s:
    print(s.index('p'))
print(s.find('p'))
print(s.replace('P', 'p'))
print(s)
s1 = 3*s
print(s1.replace('P', 'p', 1))
print(s1)
print(s1.startswith('H'))
print(s1.endswith(s))
i = s1.find('P')
if i > -1:
    print(s1[:i+1]+s1[i+1:].replace('P', 'p', 1))

for ch in s:
    print(ch)

for n in range(5):
    print(n, end=' ')
print()

for n in range(-5, 11, 2):
    print(n, end=' ')
print()

for x in np.arange(0.1, 10, 3):
    print(x, end=' ')
print()

sodd = seven = 0
for n in range(-5, 10):
    print(n, end=' ')
    if n % 2 == 0:
        seven += n
    else:
        sodd += n

print('\nSum of Odd:', sodd, 'Sum of Even:', seven)

sodd = seven = 0
for i in range(10):
    n = random.randint(-15, 10)
    print(n, end=' ')
    if n % 2 == 0:
        seven += n
    else:
        sodd += n

print('\nSum of Odd:', sodd, 'Sum of Even:', seven)

init = True
while True:
    n = int(input('n='))
    if n == 0:
        break
    if init:
        max = n
        init = not init
    elif max < n:
        max = n
if init:
    print('No data')
else:
    print('Max=', max)
