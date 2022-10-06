# import hello as h
#
# print(h.f(1))


# def new_string(symbol, count=3):
#     return symbol * count
#
#
# # print(new_string('!', 5))
# # print(new_string('!'))
# print(new_string(4))

# def concantenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
#
# print(concantenatio('a','s', 'd', 'w'))     #asdw
# print(concantenatio('a','1', 'd', '2'))     #a1d2
# # print(concantenatio(1, 2, 3, 4))          #TypeError


# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)
#


# a = (3, 4, 1, 5)
# # print(a)
# # print(a[-3])
#
# for item in a:
#     print(item)


# dictionary = {}
# dictionary = \
#     {
#         'up': 'vverh',
#         'left': 'vlevo',
#         'down': 'vniz',
#         'right': 'vpravo'
#     }
# print(dictionary['up'])
# dictionary['up'] = 'up'
# print(dictionary['up'])
# print(dictionary)
# print(dictionary['left'])


# colours = {'red', 'green', 'blue'}
# print(colours)
# print(type(colours))
# colours.add('red')
# print(colours)
# colours.add('grey')
# print(colours)
# colours.remove('red')
# print(colours)
# colours.discard('red')
# print(colours)
# colours.clear()

#
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# print(c)
# u = a.union(b)
# print(u)
# i = a.intersection(b)
# print(i)
# dl = a.difference(b)
# print(dl)
# dl =b.difference(a)
# print(dl)
#
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
#
# s = frozenset(a)        #неизменяемое множество


# list1 = [1, 2, 3, 4, 5]
# list2 = list1
#
# # for e in list1:
# #     print(e)
# #
# # print()
# #
# # for e in list2:
# #     print(e)
# #
#
# list1[0] = 123
# list2[1] = 333
# for e in list1:
#     print(e)
#
# print()
#
# for e in list2:
#     print(e)


list1 = [1, 2, 3, 4, 5]

# print(len(list1))
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)

# print(list1.pop(2))
# print(list1.insert(2, 11))
print(list1.append(11))
print(list1)
