#n입력받기
n = int(input())

x,y = 1,1 #시작점
plans = input().split()


#     l r u d에 따른 방향 이동
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move = ['l','r','u','d']


for plan in plans:
    for i in range(len(move)):#0 1 2 3
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            print(i, "// ", plan, " // dx ", dx[i], " dy ", dy[i], "//  nx ", x, " ny ", y)
    if nx<1 or ny < 1 or nx >n or ny > n:
        continue
    x, y = nx, ny


print(x, y)