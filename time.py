from random import randint
import time

#배열에 10,000개의 정수를 삽입

array = []
for _ in range(10000):
    array.append(randint(1, 100)) #1부터 100까지의 랜덤한 정수

#선택 정렬 프로그램 성능 측정
start_time = time.time()

#선택정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #스와프

end_time = time.time()

print("선택정렬 성능측정 : ", end_time - start_time)



#배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
    array.append(randint(1,100))

#파이썬 기본 정렬 라이브러리 성능 측정
start_time = time.time()

array.sort()

end_time = time.time()
print("파이썬 기본 라이브러리 소팅 : ", end_time - start_time)

