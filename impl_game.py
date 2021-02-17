#n, m을 공백으로 구분하여 입력받기
n,m = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]

#현재 캐릭터의 x좌표, y좌표, 방향을 입력
x, y, direction = map(int, input().split())

d[x][y] = 1 #현재 좌표(시작지점) 방문 처리

#전체 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0] # 위아래 이동
dy = [0, 1, 0, -1] # 좌우 이동

#왼쪽으로 회전
# direction : 0 - 북, 1 - 동, 2 - 남, 3 - 서
def turn_left():
    global direction
    direction -= -1
    if direction == -1:
        direction = 3

#시뮬레이션 시작
count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1 # 방문 표시
        x = nx # 현재 캐릭터의 좌우 위치 수정
        y = ny # 현재 캐릭터의 상하 위치 수정
        count += 1 #이동 횟수 증가
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1 # 한번 더 왼쪽으로 회전한다.
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x-dx[direction]
        ny = y-ny[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막혀있는 경우
        else:
            break # 네 방향 모두 갈 수 없고 뒤도 바다로 막혀있다면 게임 종료
        turn_time = 0


print(count)
