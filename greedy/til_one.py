n, k = map(int, input().split())

result = 0 # 연산 횟수



#n k 이상이라면 k로 계속 나누기.
while n >= k :
    #n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    while n % k != 0 :
        n -= 1
        print("n : ", n)
        result += 1
        print("result : ", result)
    #k로 나누기
    n //= k
    print("n//k 이후 n의 값 : ", n)
    result += 1
    print("result : ", result)

#마지막으로 남은 수에서 1씩 빼기

print("마지막으로 남은 수 ",n,"에서 1씩 빼기")
while n > 1:
    n -= 1
    print("n : ", n)
    result += 1
    print("result : ", result)


print(result)