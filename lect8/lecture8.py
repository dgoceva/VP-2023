import sys


def file_sizes(arg):
    result = False
    try:
        f = open(arg, 'r')
        print('File', arg, 'has size', len(f.readlines()))
        f.close()
    except FileNotFoundError as e:
        print('No such file', arg)
    except OSError as e:
        print(e)
    else:
        result = True
    finally:
        return result


# while True
#     x=input()

# ZeroDivisionError
# x = 1/0
# print(x)

# ValueError
# x = int(input('x='))
# print(x)

# FileNotFoundError
# f = open('abc')
# print(f.read())

# x = 0
# try:
#     x = int(input('x='))
# except ValueError:
#     print('Not a valid number')
# print(x)

# while True:
#     try:
#         x = int(input('x='))
#         break
#     except ValueError:
#         print('Not a valid number')
# print(x)

# while True:
#     try:
#         x = int(input('x='))
#         y = 1/x
#         break
#     except (ValueError, ZeroDivisionError):
#         print('Not a valid number')
# print(x, y)

# while True:
#     try:
#         x = int(input('x='))
#         name = input('file name: ')
#         y = 1/x
#         f = open(name)
#         length = len(f.readlines())
#         f.close()
#         break
#     except ValueError:
#         print('Not a valid number')
#     except ZeroDivisionError:
#         print('Division by zero')
#     # except FileNotFoundError:
#         # print('No file ', name)
#     except:
#         print('Unknown error')
# print(x, y, length)
# print(sys.argv)
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#         print('File', arg, 'has size', len(f.readlines()))
#     except FileNotFoundError as e:
#         print('No such file')
#         # raise
#         raise ValueError
#     except OSError as e:
#         print(e)
#     else:
#         f.close()
for arg in sys.argv[1:]:
    print(file_sizes(arg))
