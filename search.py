# 탐색 (search): 많은 양의 데이터 중 원하는 데이터를 찾는 과정을 뜻한다.
# 프로그래밍에선 주로 그래프, 트리 등의 자료구조 내에서 행해지며 대표적으로 DFS (Depth-First) & BFS (Breadth-First) 가 있다.
# 이 두 methods 를 이해하기 위해선 기본 자료구조인 스택 (stack) & 큐 (queue) 에 대한 이해가 있어야 한다.

# 자료구조 (Data Structure): 데이터를 표현, 관리, 처리하기 위한 구조를 의미하며 그중 스택 & 큐는 자료구조의 기초개념으로 다음 핵심함수들로 구성된다.
# - 삽입 (Push): 데이터를 삽입한다.
# - 삭제 (Pop): 데이터를 삭제한다. 

# 스택과 큐를 사용할 때엔 삽입과 삭제 외에 오버플로 (overlfow) 와 언더플로 (underflow) 를 고민해야 한다.
# - 오버플로 (Overflow): 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 채운 상태에서 삽입연산을 수행할 때 발생한다.
# - 언더플로 (Underflow): 특정한 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행하면 데이터가 전혀 없는 상태이므로 발생한다.


# 스택
# 아래에서부터 위로 차곡차곡 쌓고 아래에 있는 박스를 치우기 위해선 그 위의 박스를 내려야 한다는 특징이 있는 박스 쌓기와 유사하다.
# 이러한 구조를 선입후출 (First In Last Out) 구조, 또는 후입선출 (Last In First Out) 구조라 한다.

# 스택 예제:
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])

# [5, 2, 3, 1]
# [1, 3, 2, 5]

# 큐
# 큐는 선입선출 (First In First Out) 인 대기 줄에 비유할 수 있으며, 고로 공정하다 표현한다.

from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용한다.
# deque 은 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리 보다 간단하다.
# deque 객체를 리스트 자료형으로 변경하고자 한다면 list() method 를 이용하자 - list(queue) 를 하면 리스트가 반환된다.

# 재귀함수
# DFS 와 BFS 를 구현하려면 재귀 함수 (Recursive Function) 에 대한 이해가 필요
# 재귀 함수 (Recursive Function): 자기 자신을 다시 호출하는 함수를 의미

# 예:
# def recursive_function():
#     print('재귀 함수를 호출합니다.')
#     recursive_function()
#
# recursive_function()

# 이 코드는 '재귀 함수를 호출합니다.' 라는 문자열을 무한히 출력한다.
# 어느 정도 출력하다가 Recursion Error 를 출력하고 멈출 것임.

# 재귀함수의 종료 조건:
# 재귀 함수를 사용할 때는 종료 조건을 꼭 명시해야 하는데 그러지 않음 함수가 무한 호출됨.

def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출')
    recursive_function(i + 1)
    print(i, '번째 재귀 함수를 종료')

recursive_function(1)

# 재귀 함수를 계속해서 호출했을 때 가장 마지막에 호출한 함수 (recursive_function(100))
# 가 먼저 수행을 끝내야 그 앞의 함수 호출 (recursive_function(99)) 의 호출이 종료되기 때문에
# 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용한다 (그렇지 않았음 1-99 호출, 1-99 종료)
# 재귀 함수는 내부적으로 스택 자료구조와 동일하기에 스택 자료구조를 활용해야 하는 상당수의 알고리즘은
# 재귀 함수를 이용해 간편하게 구현될 수 있다. DFS 가 대표적인 예.

# 재귀 함수를 이용하는 대표적 예제로는 팩토리얼 (Factorial) 문제가 있다

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1 부터 n까지 차례로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n * (n-1)! 를 그대로 작성
    return n * factorial_recursive(n-1)

print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))

# 재귀 함수의 코드가 더 간결한 이유는 재귀 함수가 수학의 점화식 (재귀식)을
# 그대로 소스코드로 옮겼기 때문이다. 이때 점화식은:
# 특정한 함수를 자신보다 더 작을 변수에 대한 함수와의 관계로 표현한 것을 의미한다.

# 탐색 알고리즘 DFS/BFS
# DFS (Depth-First Search): 깊이 우선 탐색으로도 불리우는, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# 그래프는 노드 (node) 와 간선 (edge) 로 표현되며 이때 노드를 정점 (vertex) 라고도 말한다.
# 만약 두 노드가 간선으로 연결되어 있다면 두 노드는 인접 (adjacent) 하다 한다.

# 프로그래밍에서 그래프는 크게 2가지 방식으로 표현할 수 있는데 코딩 테스트에서는 이 두 방식 모두 필요:
# 1. 인접 행렬 (Adjacency Matrix): 2차원 배열로 그래프의 연결 관계를 표현하는 방식
# 2. 인접 리스트 (Adjacency List): 리스트로 그래프의 연결 관계를 표현하는 방

# 예:
#       0
#   7 /   \ 5
#   1      2

#     0   1   2
# 0   0   7   5
# 1   7   0   INF
# 2   5   INF 0

# Adjacency Matrix:
INF = 999999999
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# Adjacency List:

# Print a 3 x 1 matrix
graph = [[] for _ in range(3)]

# Save info (node, distance) of the node(s) connected to node 0
graph[0].append((1, 7))
graph[0].append((2, 5))

# Same for node 1
graph[1].append((0, 7))

# Same for node 2
graph[2].append((0, 5))

print(graph)

# Adjacency Matrix vs. Adjacency List
# 인접 행렬 (Adjacency Matrix) 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비된다.
# 반면에 인접 리스트 (Adjacency List) 방식은 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용한다.
# 하지만 이와 같은 속성 때문에 인접 리스트 방식은 인접 행렬 방식에 비해 특정한 두 노드가 연결되어 있는지에 관한
# 정보를 얻는 속도가 느리다. 인접 리스트 방식에서는 연결된 데이터를 하나씩 확인해야 햐기 때문이다.

# DFS (Depth-First Search); 깊이 우선 탐색
# 특정한 경로로 탐색하다 특정한 상황에서 최대한 깊숙이 들어가 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색하는 알고리즘.
# Analogy: 갈림길에서 선택한 후 그 가지에서 탐색할 만큼 탐색한 후 더 이상 방문해 볼 곳이 없음 갈래길로 돌아가 다른 갈림길 선택.
# Formal steps:
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
# 2. 스택의 최산단 노드, 즉 1에서 삽입한 노드에 방문하지 않은 인접 노드가 있으면 1의 노드 위에 얹어 방문 처리를 한다.
#    방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 이 과정을 더 이상 수행할 수 없을 때까지, 즉 모든 노드를 방문하였을 때까지 반복한다.

# BFS (Breadth-First Search); 너비 우선 탐색
# 가장 가까운 노드부터 탐색하는 알고리즘으로서 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작하는 BFS 와 반대개념.
# BFS 는 선입선출 방식인 큐 자료구조를 이용하는 것이 정석이다.
# 동작방식:
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
# 2. 큐에서 노드 하나를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
# 3. 위의 과정을 더 이상 수행할 수 없을 때까지 수행.

# 너비 우선 탐색 알고리즘인 BFS는 큐 자료구조에 기초한다는 점에서 구현이 간단하다.
# 실제로 구현함에 있어 앞서 언급한 대로 deque 라이브러리를 사용하는 것이 좋으며 탐색을 수행함에 있어 O(N) 이 소요.
# 수행시간은 DFS보다 좋은 편이라는 장점이 있다.

# BFS Example:
from collections import deque

# Define BFS Method
def bfs(graph, start, visited):
    # Use deque library for simulating Queue
    # A list goes into the deque function so [1]
    queue = deque([start])
    # Mark the present node visited
    visited[start] = True
    # Repeat until queue is empty
    while queue:
        # Pull one node from queue and print
        v = queue.popleft()
        print(v, end=' ')
        # Insert unvisited elements adjacent to the node
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# Express graph as adjacency list
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# Initiate the 'visited' list
visited = [False] * 9

# Call BFS
bfs(graph, 1, visited)


# Example 2

from collections import deque

# Receive map dimensions n, m
n, m = map(int, input().split())

# Receive map info
graph = []
for i in n:
    graph.append(list(map(int, input().split())))

# Define directional increments
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# Define DFS function
def dfs(x, y):
    queue = deque()
    queue.append(x, y)
    # Repeat until queue is empty
    x, y = queue.popleft()
    # Check four directions
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # Ignore if out of map
        if nx < 0 or ny < 0 or nx >= n >= m:
            continue
        # Ignore if wall
        if graph[nx][ny] == 0:
            continue
        # Record if unvisited
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))
    # Return distnace
    return graph[n-1][m-1]

# Print BFS result
print(bfs(0, 0))