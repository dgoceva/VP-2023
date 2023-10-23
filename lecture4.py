
from collections import deque

data = [-1, 10, 11, -32, 15]
print(data)
data.sort()
print(data)

data = [
    [1, 2, 3],
    [4, 5]
]
print(data)
for i in range(2):
    for j in range(len(data[i])):
        print(data[i][j], end=' ')
    print()

data = [
    [123, 'Lili', 5.65],
    [222, 'Ivan', 5.33],
    [333, 'Petyr', 5.47]
]
print(data)
data.sort(key=lambda st: st[2])
print(data)
data.sort(key=lambda st: st[1], reverse=True)
print(data)

print(sorted(data, key=lambda st: st[0]))
print(sorted.__doc__)
# print(print.__annotations__)

# EURO = 1.95576
# currency_in = input('Currency: ').upper()
# value_in = float(input('Value: '))
# if currency_in == 'BGN':
#     currency_out = 'EUR'
#     value_out = value_in*EURO
# elif currency_in == 'EUR':
#     currency_out = 'BGN'
#     value_out = value_in/EURO
# else:
#     print('Not supported...')
#     exit()
# print(value_out, currency_out)

stack = [1, 2, 3]
stack.append(44)
print(stack)
print(stack.pop())
print(stack)

queue = [1, 2, 3]
queue.insert(0, 44)
print(queue)
print(queue.pop(0))
print(queue)

deque = deque([1, 2, 3])
deque.appendleft(44)
deque.append(55)
print(deque)
print(deque.pop())
print(deque)
print(deque.popleft())
print(deque)

data = [int(x) for x in input('Data: ').split(',')]
print(data)
