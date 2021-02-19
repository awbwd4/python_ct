import sys

f = open('C:\\Users\\JaeukKo\\Desktop\\trading_algorithm\\readme.txt')
lines = f.readlines()

# sys.stdout.writelines(lines[:5])

# sys.stdout.writelines(lines[15:20])


sys.stdout.writelines(lines[-5:])