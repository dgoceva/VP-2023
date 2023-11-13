f = open('lecture6.py')
print(f.read())
f.close()

f = open(r'lect7\lecture7.py', 'r')
print(f.readline())
for line in f:
    print(line, end='')
f.close()

count = 0
with open('lecture5.py') as f:
    for line in f:
        print(line.upper(), end='')
        count += 1
print('Number of rows: %d' % count)

with open('lect7\\data.txt') as f:
    l = [int(x) for x in f.readline().split()]
print(l)

with open('lect7\\out.txt', 'w') as f:
    for x in l:
        f.write(str(x)+' ')

with open('lect7\\out.txt', 'a') as f:
    for x in l:
        f.write(str(x)+'\n')
