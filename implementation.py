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

# 예제 4-3: 게임 개발
# 문제: 1 x 1 의 정사각형으로 이뤄진 N x M 크기의 직사각형 맵이 있다.
# 각각의 칸은 츅지 또는 바다이고 캐릭터는 동서남북 중 한 곳을 바라본다.
# 맵의 각 칸은 (A, B) 로 나타내며 A는 북쪽으로부터, B는 서쪽으로부터 떨어진 칸의 개수이다.
# 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.

# 캐릭터 매뉴얼:
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정함.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 전진함.
# 3. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 하고 1단계로 돌아감.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로
#    한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 멈춘다.

# 중요 테크닉:
# 문제에선 각 방향을 나타내는 정수를 다음과 같이 명시한다:
# - 0: 북쪽
# - 1: 동쪽
# - 2: 남쪽
# - 3: 서쪽
# 일반적으로 방향을 설정해서 이동하는 문제 유형에서는 dx, dy 라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적
# 예를 들면, 현재 캐릭터가 북쪽을 바라보고 있을 때는 북쪽으로 이동하기 위해 x, y 좌표를 각각 dx[0], dy[0] 씩 더함

# Receive N x M
n, m = map(int, input().split())

# Create a map to record character movement
d = [[0] * m for _ in range(n)]
# Receive current character orientation
x, y, direction = map(int, input().split())
d[x][y] = 1

# Receive entire map info
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# Define N, E, S, W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# Turn left
def turn_left:
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# Begin simulation
count = 1
turn_time = 0
while True:
    # Turn left
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # If there is an unexplored space ahead, onward
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    # If there is no unexplored land or there's the ocean
    else:
        turn_time += 1
    # Can't go either direction
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # If you can go backward, do so
        if array[nx][ny] == 0:
            x, y = nx, ny
        # If not
        else:
            break
        turn_time = 0

# Print output
print(count)