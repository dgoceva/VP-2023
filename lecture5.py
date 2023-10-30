t1 = (1, 2, 3)
print(t1)
# t1[1] = (11, 12)
# t1[0:2] = (22, 33, 44)
t1 = (1, 2, 22, 33, 3)
print(t1)
# t1.append(33)
print(t1[1], t1[2:5])
# t1.remove(1)
# del t1[1]
# del t1[:]
del t1

t1 = (1, 2, 3)
print(t1)
a, b, c = t1
print(a, b, c)

t1 = ()
print(t1)
t1 = (1)
print(type(t1), t1)
t1 = (1,)
print(type(t1), t1)

l1 = [1, 2, 3]
l1[1] = [11, 12]
l1[0:2] = [22, 33, 44]
l1.append(33)
print(l1)
print(l1[1], l1[2:5])
if -1 in l1:
    l1.remove(-1)
l1.remove(22)
print(l1)

del l1[0]
print(l1)
del l1[1:3]
print(l1)
del l1[:]
print(l1)
del l1
# print(l1)

# set
# frozenset
s1 = set()    # {} NO! This is empty dictionary
print(s1)
s1 = {1, 2, 3, 4, 5}
print(type(s1), s1)
s2 = {1, 2, 4, 55, 44}
print(s1-s2)
print(s2-s1)
print(s1 | s2)
print(s1.union(s2))
print(len(s1))
print(66 not in s1)
print(s1.symmetric_difference(s2))
print(s1.intersection(s2))

year = input('year: ')
print(set(year))
print(list(year))
print(tuple(year))
year1 = int(year)
while True:
    year1 += 1
    if (len(tuple(str(year1))) == len(set(str(year1)))):
        break
print(year, '->', year1)

print(s1)
s1.add(111)
# s1.append(222)
s1.update([11, 22, 33])
if 333 in s1:
    s1.remove(333)
print(s1)

# print(s1[1])
for n in s1:
    print(n)

l1 = list(s1)
# for n in reversed(s1):
for n in reversed(l1):
    print(n, end=' ')
print()

for n in sorted(s1):
    print(n, end=' ')
print()

for n in reversed(sorted(l1)):
    print(n, end=' ')
print()

for i, n in enumerate(s1):
    print(i, '->', n, end=' ')
print()

s2 = {ch.upper() for ch in 'abcDEFxy12'}
print(s2)

t1 = (1, 2, 3, 4, 5)
# t2 = (x**3 for x in t1)
t2 = tuple([x**3 for x in t1])
print(t2)

d1 = {}
print(type(d1))
d1 = {1: 1, 2: 3, 3: 9}
print(d1)
l2 = list(d1)
print(l2)
d1[4] = 16
print(d1)
if 5 in l2:
    print(d1[5])
print(d1[4])

if 6 in d1.keys():
    print(d1[6])

d2 = {1: 'one', 2: 'two', 3: 'three'}
print(d2)

del d1[2]
print(d1)

d3 = {x: x**2 for x in (1, 2, 3, 4)}
print(d3)

for k, v in d3.items():
    print(k, '->', v, end='  ')
print()
