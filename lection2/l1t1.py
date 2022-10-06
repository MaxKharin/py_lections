# colours = ['red', 'green', 'blue2132']
# data = open('file.txt', 'w')
# # data.writelines(colours)
# data.write('\nLINE2\n')
# data.write('LINE3\n')
# data.close()
#

# with open('file.txt', 'a') as data:
#     data.write('line uyuyg1\n')
#     data.write('line 2,mnlkn\n')

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
