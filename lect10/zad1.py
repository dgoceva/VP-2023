import random


def myinput(prompt, low, high):
    while True:
        try:
            number = int(input(prompt))
            if number <= low or number >= high:
                raise ValueError("Invalid number...")
            else:
                return number
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    n = myinput("n=", 15, 35)
    mylist1 = []
    for i in range(n):
        # mylist1.append(myinput(f"{i+1}=", 30, 300))
        mylist1.append(random.randint(30, 300))
    # print(mylist1)
    mylist11 = [x for x in mylist1 if x//10 % 10 % 3 == 0]
    # print(mylist11)
    print(len(mylist11))

    mylist12 = [x for x in mylist1 if x % 6 == 4]
    # print(mylist12)
    min1 = min(mylist12)
    index = mylist1.index(min1)
    print(min1, index)

    mylist2 = [x for x in mylist1 if 9 < x <
               100 and (x % 2 == 0 or x % 3 == 0)]
    print(mylist2)
    mylist22 = [mylist2[i] for i in range(1, len(mylist2), 2)]
    # print(mylist22)
    try:
        print(sum(mylist22)/len(mylist22))
    except ZeroDivisionError as e:
        print(e)
    mylist23 = [x for x in mylist2 if x % 2 == 0]
    # print(mylist23)
    try:
        min_even = min(mylist23)
        print(min_even)
        mylist2.remove(min_even)
        print(mylist2)
    except ValueError:
        print("No such data...")
