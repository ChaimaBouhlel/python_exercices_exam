"""def fun(*data):
    for i in data:
        print(i)


fun(1)
fun(1, 2, 3)"""

"""def display(**kwargs):
    for i in kwargs:
        print(i, kwargs[i])


display(emp="Kelly", salary=9000)
"""

"""def fun1(name, age):
    print(name, age)


fun1("Emma", age=23)
fun1("Emma", 23)"""

"""def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)
    return a


result = outer_fun(5, 10)
print(result)"""

"""def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)


res = outer_fun(5, 10)
print(res)"""


def func(p1, p2="hello"):
    print(p1, p2)


func(p2="bonjour", p1="hello")

l = [1, 2, 3, 4, 5, 6, 7]
print(l[:-3])
