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
        result += i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n * (n-1)! 를 그대로 작성
    return n * factorial_recursive(n-1)

print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))