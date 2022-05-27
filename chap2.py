"""liste = [2, 2, 8, 9]
slice_liste = liste[-1]
print(slice_liste)"""

"""d = dict({
    ('foo', 100),
    ('bar', 200),
    ('baz', 300)
})

d[len(d)] = 23
print(d)
d.pop(3)
print(d)
d2 = {}
d2.update(d)
print(d2)

for key in d:
    print(key)

l = ["liste", "avec", "des", "mots"]

i = 0
for key in d2:
    d2[key] = l[i]
    i += 1

print(d2)

print(d2.items())
print(d2.keys())
for value in d2.values():
    print(value)

d1 = {len(e): e for e in l}
print(d1)"""

"""tup = (1, 1, 1)
print(tup)

"""
"""a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
d_items = a_dict.items()
print(d_items)"""

"""prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for key in prices.keys():
    if key == 'orange':
        del prices[key]"""

"""a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {value: key for key, value in a_dict.items()}
print(new_dict)"""

"""integers = [1, 2, 3]
letters = ['a', 'b', 'c']
floats = [4.0, 5.0, 6.0]
zipped = zip(integers, letters, floats)  # Three input iterables
print(list(zipped))"""

"""objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']

a_dict = {key: value for key, value in zip(categories, objects)}
print(a_dict)

lco = list(zip(categories, objects))
for key, value in lco:
    print(key, value)"""

"""a_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items() if v <= 2}
print(new_dict)
"""
"""a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(max(a[2:4] + ['grault']))
print(a[2:4])
print(a[-5:-3])
print(a[:] is a)
print(a[-6])
print(a[1::2])
a[2:2] = []
print(a)
a[2] = []
print(a)
a.remove([])
print(a)
a += 'de'
print(a)
a[len(a):] = ['d', 'e']
print(a)
a.extend(['d', 'e'])
print(a)
a.append(['d', 'e'])
print(a)
"""
a = [1, 2, 7, 8]
a[2:3] = [3, 4, 5, 6, 7]
print(a)

x = 5
y = -5
x, y = (y, x)[::-1]
print(x, y)
