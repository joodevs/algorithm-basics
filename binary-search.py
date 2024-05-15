# 순차 탐색 (Sequential Search)
# 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법.
# 보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용함.
# 리스트 내에 데이터가 아무리 많아도 시간만 충분하다면 항상 원하는 원소를 찾을 수 있다는 장점이 있음.
# 데이터의 개수가 N개일 때 최대 N번의 비교 연산이 필요하므로 순차 탐색의 최악의 경우 시간 복잡도는 O(N).

# Declare algorithm
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

# UI
print('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입렬하세요.')
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print('앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.')
array = input().split()

# Result
print(sequential_search(n, target, array))


# 이진 탐색 (Binary Search)
# 내부의 데이터가 정렬되어 있을 때 탐색 범위를 절반씩 좁혀가며 매우 빠르게 데이터를 찾을 수 있음.
# 위치를 나타내는 변수 3갸를 이용하는데, 탐색학고자 하는 범위의 시작점, 끝점, 그리고 중간점이다.
# 원리는 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 (재귀적) 비교해 원하는 데이터를 찾는 것.

# Declare algorithm - Recursion
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # If found:
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# UI
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# Print result
result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)

# # Declare algorithm - Repetition
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None
#
# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))
#
# result = binary_search(array, target, 0, n - 1)
# if result == None:
#     print('원소가 존재하지 않습니다.')
# else:
#     print(result + 1)

# 코딩 테스트에서의 이진 탐색
# 코딩 테스트에서의 이진 탐색 문제는 탐색 범위가 큰 상황에서의 탐색을 가정하는
# 문제가 많다. 따라서 탐색 범위가 2,000만을 넘어가면 이진 탐색을 권한다.
# 처리해야 할 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 이진 탐색과 같이
# O(logN)의 속도를 내야 하는 알고리즘을 이용해 풀어야 하는 경우가 많다.


# 트리 자료구조
# 트리 자료구조는 노드와 노드의 연결로 표현하며, 노드는 정보의 단위로서 어떠한 정보를
# 갖고 있는 개체로 이해할 수 있다. 트리는 그래프 자료구조의 일종으로 데이터베이스
# 시스템이나 파일 시스템과 같은 곳에서 많은 양의 데이터를 관리하기 위한 목적으로 사용한다.

# 주요특징:
# - 트리는 부모 노드와 자식 노드의 관계로 표현된다.
# - 트리의 최상단 노드를 루트 노드라고 한다.
# - 트리의 최하단 노드를 단말 노드라고 한다.
# - 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라 한다.
# - 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다.

# 정리하자면 큰 데이터를 처리하는 소프트웨어는 대부분 데이터를 트리 자료구조로 저장해
# 이진탐색과 같은 탐색 기법을 이용해 빠르게 탐색이 가능하다.

# 이진 탐색 트리
# 트리 자료구조 중 가장 간단한 형태가 이진 탐색 트리다.
# 형태는 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드

# 빠르게 입력 받기
# 데이터의 개수가 많은 문제에 input() 함수를 이용하면 동작 속도가 느려
# 오답 판정을 받을 수 있다. 이 같은 경우엔 sys 라이브러리의 readline()!

import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)


# 실전 문제 - 부품 찾기
# 동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가
# 있다. 어느 날 손님이 M개 종휴의 부품을 대량으로 구매하겠다며 당일 날 견적서를
# 요청했다. 동ㅇ빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해
# 견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램.

# 예를 들어 가게의 부품이 총 5개일 때 부품 번호가 다음과 같다고 하자.
# N = 1
# [8, 3, 7, 9, 2]
# M = 3
# [5, 7, 9]

# 이진 탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 계수 정렬
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')