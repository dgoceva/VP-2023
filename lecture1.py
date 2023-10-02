import math

a = 5
b = 4.3
c = 'Hello '
d = 2
print(a, b, c)
print(a+b)
print(str(a)+c)
print(a**d)
print(a//d)
print(a/d)
print(a % d)
print(3*c)

# < <= > >= == !=
print(a < b)
print(a != d)

# X         Y       and     or      not Y
# False     False   False   False   True
# False     True    False   True    False
# True      False   False   True    -----
# True      True    True    True    -----

print(a < b and a == d)
print(2 == '2')
print(not False)

a = input()
print(a, type(a))
a1 = input('Enter a1:')
print(a1)
print(a+a1)
print(int(a)+int(a1))
b = float(input('b='))
print(b, type(b))
print(0.1+0.2)

a, b, c = map(int, input('Data:').split())
print(a, b, c, type(a))

a = complex(2, 3)
print(a)
b = 3+4j
print(b, type(b))

a = float(input('a='))
b = float(input('b='))
c = float(input("c="))
if a == 0:
    print('a==0')
else:
    D = b*b - 4*a*c
    if D > 0:
        a1 = (-b - math.sqrt(D))/(2*a)
        a2 = (-b + math.sqrt(D))/2/a
        print("a1=%.2f a2=%.3f" % (a1, a2))
    elif D == 0:
        a2 = a1 = -b/(2*a)
        print('a1={0} a2={1}'.format(a1, a2))
    else:
        print('No real answer')
