# 예제 4-1: 상하좌우

# 문제: N x N 크기의 정사각형 그리드 위에서 [L, R, U, D] 인풋에 따라 좌우로 이동한다.
#      이때, 시작점은 (1, 1) 이며 그리드 밖으로 이동하게 만드는 커맨드는 무시한다.

# 내 답안:

# Receive inputs
n = int(input())
plans = input().split()

x, y = 1, 1

# Movement according to L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
command_types = ['L', 'R', 'U', 'D']

# Iterate through each plan and compare with command types
for plan in plans:
    for i in range(len(command_types))
        if plan == command_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # Ignore if person escapes the map
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # Move
        x, y = nx, ny

print(nx, ny)