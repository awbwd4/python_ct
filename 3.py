def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result


result = two_times([1,2,3,4])

print(result)


def two_times(x):
    return x*2

result2 = list(map(two_times, [1,2,3,4]))

map(two_times, [1,2,3,4])

print(result2)

print(map(two_times, [1,2,3,4]))


result3 = list(map(lambda a : a*3, [2,3,4,5,6]))

print(result3)