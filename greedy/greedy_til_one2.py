n, k = map(int, input().split())
result = 0


while True :
    #(n == k로 나누어 떨어지는 수가 될 때 까지 1씩 빼기
    target = (n//k)*k
    result += (n-target)
    n = target # n이 k의 배수가 됨.
    print("n = target 일 때 n의 값 : " , n)
    print("이 시점에서 result 값 : ", result)
    #n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    #k로 나누기
    result += 1
    n //= k


# 마지막으로 남은 수에 대하여 1씩 빼기
print("마지막으로 남은 n ", n)
result += (n-1)

print("result")