# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))
#
# print(numbers)
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)

# colours = ['red', 'green', 'blue']
#
# for e in colours:
#     print(e)                                            #red green blue
#
# for e in colours:
#     print(e * 2)                                        #redred greengreen blueblue
#
# colours.append('grey')                                  #добавить в конец
# print(colours == ['red', 'green', 'blue', 'grey'])      #True
# colours.remove('red')                                   #del colours[0] # удалить элемент

def f(x):
    if x == 1:
        return 'Integer'         #Str
    elif x == 2.3:
        return 23                #Int
    else:
        return                   #NoneType

arg = 3
print(f(arg))
print(type(f(arg)))