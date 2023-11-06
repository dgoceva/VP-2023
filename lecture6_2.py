from functools import reduce
import numpy as np

data = [int(x) for x in input('Data: ').split()]
print(data)

print(sum(data))

print(reduce(lambda x, y: x*y, data))

print(np.prod(data))

even = [x for x in data if x % 2 == 0]
print(even)

print(np.prod(even))
print(np.sum(even))

print(np.min([x for x in data if x % 2 != 0]))
print(max(even))
