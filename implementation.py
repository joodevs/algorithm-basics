# 예제 4-1: 상하좌우
# 문제: N x N 크기의 정사각형 그리드 위에서 [L, R, U, D] 인풋에 따라 좌우로 이동한다.
#      이때, 시작점은 (1, 1) 이며 그리드 밖으로 이동하게 만드는 커맨드는 무시한다.

# 내 답안:

# Receive inputs
n = int(input())
plans = input().split()

x, y = 1, 1
nx, ny = 0, 0

# Movement according to L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
command_types = ['L', 'R', 'U', 'D']

# Iterate through each plan and compare with command types
for plan in plans:
    for i in range(len(command_types)):
        if plan == command_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # Ignore if person escapes the map
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # Move
        x, y = nx, ny

print(nx, ny)

# 예제 4-2: 시각
# 문제: 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
#      모든 경우의 수를 구하는 프로그램을 작성하시오.

# 내 풀이
n = int(input())
count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

# 예제 4-3: 왕실의 나이트
# 문제: 8 x 8 체스판에서 나이트는 2 x 1 만큼 이동할 수 있다.
#      나이트의 현 위치가 주어졌을 때 이동할 수 있는 경로의 경우의 수를 출력하라.

# Receive current position
pos = input()
row = int(pos[1])
col = int(ord(pos[0]) - ord('a')) + 1

# Define possible movements
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

# Check if movement is possible
counter = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    # Increase counter if possible
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        counter += 1

print(counter)

# 앞서 '상하좌우' 문제에서는 dx, dy 리스트를 선언하여 이동할 방향을 기록할 수 있도록 하였다면
# 이번 소스코드에서는 steps 변수가 dx와 dy 변수의 기능을 대신하여 수행한다.
# 2가지 형태 모두 자주 사용되므로, 참고하도록 하자.