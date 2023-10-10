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