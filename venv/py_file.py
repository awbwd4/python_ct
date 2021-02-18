# from builtins import print

f = open('C:\\Users\\JaeukKo\\Desktop\\trading_algorithm\\buy_list.txt','rt',encoding='UTF-8')


f.readlines()

lines = f.readlines()
print(lines)

# for line in lines:
#     print(line)


f = open('C:\\Users\\JaeukKo\\Desktop\\trading_algorithm\\python_fun.txt')
# print(f.read())
buffer = f.read()
print(buffer)


letter = open("C:\\Users\\JaeukKo\\Desktop\\trading_algorithm\\letter.txt", 'w')
letter.write('dear father,')
letter.close()


letter = open("C:\\Users\\JaeukKo\\Desktop\\trading_algorithm\\letter.txt", 'a+')
letter.write('\n\nHow are you?')
letter.close()


f=open('C:\\Users\\JaeukKo\\Desktop\\trading_algorithm\\readme.txt', encoding='UTF-8')

print(f.readline())
print(f.readline())

for x in range(5):
    line = f.readline()
    print(line)