abc = 10


def outer_scope1():
    abc1 = 1000

    def outer_scope():
        abc = 20

        def inner_scope1():
            abc = 30
            print('local abc:', abc)

        def inner_scope2():
            nonlocal abc, abc1
            abc = 100
            abc1 = 2000
            print('nonlocal abc: ', abc)

        def inner_scope3():
            global abc
            abc = 40
            print('global abc: ', abc)
        inner_scope1()
        print('outer local abc: ', abc)
        inner_scope2()
        print('outer local abc: ', abc)
        inner_scope3()
        print('outer local abc: ', abc)
    outer_scope()
    print(abc1)


outer_scope1()
print('global abc: ', abc)
