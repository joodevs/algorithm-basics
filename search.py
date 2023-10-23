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