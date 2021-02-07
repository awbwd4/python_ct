#n, m, k를 공백으로 구분하여 입력받기
# n : 입력받을 수의 갯수
# m : 연산 가능한 최대 횟수
# k : 가장 큰 수의 연속 횟수

n,m,k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() #입력받은 수들 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

result = 0

while True :
    for i in range(k): # 가장 큰 수를 k번 더하기
        if m == 0 :
            break
        print("first : ", first)
        result += first
        print("남은 연산 횟수 : ", m)
        m -= 1 #더할 때 마다 1씩 빼기
    if m == 0: #m == 0 반복문 탈출
            break
    print("second : ", second)
    result += second # 두번째 큰 수 더하기
    print("result", result)
    print("남은 연산 횟수")
    m -= 1



print(result)