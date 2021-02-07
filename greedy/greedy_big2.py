# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# n : 선택 할 수 있는 수의 갯수
# m : 나열되는 수의 갯수
# k : 선택지 중 가장 큰 수의 연속 가능한 갯수

# n개의 수를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
sec = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
cnt = int(m/k+1) * k
cnt += m%(k+1)

result = 0
result += (cnt) * first
result += (m-cnt)*sec


print("cnt : ", cnt)
print("result : ", result)
