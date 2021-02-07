# 현재 나이트의 위치 입력받기
input_data = input()  #a1 -> a열 1행
row = int(input_data[1]) # 행 - 숫자
column = int(ord(input_data[0])) - int(ord('a'))+1 #열 - 알파벳, 해당 문자가 몇번째 문자인지 확인

column2 = int(ord(input_data[0]))
#ord : 입력된 문자의 아스키 코드값을 리턴함
#chr : 입력된 아스키코드의 문자값을 리턴함.scvsdfgsdfgs

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

#아래, 우측 - 양수 // 위, 좌측 - 음수

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    #이동하고자 하는 위치 확인
    print("step : ", step)
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
        print(">>>>>>>>>>>>>>>>result : ", result)


print(result)


