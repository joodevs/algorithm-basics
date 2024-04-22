# 정렬 (Sorting)

# 정렬 (Sorting) 이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 뜻함.
# 정렬 알고리즘은 이진탐색 (Binary Search) 의 전처리 과정이기도 함.

# 정렬 알고리즘은 굉장히 다양한데, 이 중에서 많이 사용하는 것은:
# - 선택 정렬 (Selection Sort)
# - 삽입 정렬 (Insertion Sort)
# - 퀵 정렬 (Quick Sort)
# - 계수 정렬 (Counting Sort)

# 보통 코딩테스트 문제에서 요구하는 조건에 따라 적절한 정렬 알고리즘이 공식처럼 사용되며,
# 상황에 적절하지 못한 정렬 알고리즘을 이용하면 당연히 프로그램은 비효율적으로 동작.
# 컴퓨터는 인간과는 다르게 데이터의 규칙성을 직관적으로 알 수 없으며, 어떻게 정렬을
# 수행할지에 대한 과정을 소스코드로 작성하여 구체적으로 명시해야 한다.

# 선택 정렬 (Selection Sort)
# 정의: 데이터가 무작위로 여러 개 있을 때, 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는
#      데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복
#      이 과정은 (N - 1) 번 반복됨.

# Example:
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    # Find the real minimal index in the leftover array
    for j in range(i + 1, len(array)):
        if array[j] < array[min_index]:
            # Re-iniate min_index
            min_index = j
    # Swap
    array[i], array[min_index] = array[min_index], array[i]

# 선택정렬의 시간 복잡도
# 선택정렬은 N - 1 번 만큼 가장 작은 수를 찾아 맨 앞으로 보내야 한다. 또한, 매번 가장 작은 수를
# 찾기 위해 비교 연산이 필요하다. 고로 연산 횟수는 N + (N - 1) + (N - 2) + ... + 2
# The outer loop is responsible for setting the starting point for the inner loop.
# The inner loop is responsible for iterating through the unsorted portion for comparison.
# The comparison is done (N - 1) times at first, (N - 2) after that, .. 3, 2, and 1, and
# the number of "rounds" is (N - 1), the number of iterations for the outer loop
# Bcause of this quadratic nature, the time complexity of selection sort is n^2 as found below:
# (N - 1) + (N - 2) + ... + 2 + 1 = N * (N - 1) / 2


# 삽입 정렬
# 다음 코드로 충분히 셜명이 되며, 시간 복잡도는 O(N^2) 이다.
# 다만, 선택정렬의 시간 복잡도가 항상 O(N^2) 인 것에 반해, 삽입 정렬은 최선의 경우 O(N).
# 거의 정렬되어 있는 상태로 입력이 주어지는 문제라면 삽입 정렬을 이용하는 것이 효율적.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)


# 퀵 정렬 (Quick Sort)

# 퀵 정렬은 정렬 알고리즘 중 가장 많이 사용되는 알고리즘이다.
# 퀵 정렬과 병합 정렬은 (merge sort) 는 대부분의 프로그래밍 언어에서
# 정렬 라이브러리의 근간이 되는 알고리즘이기도 하다.

# 퀵 정렬에서는 기준 (pivot) 을 설정하고 이 기준보다 큰 수와 작은 수를 교환함으로써 리스트를 반으로 나눈다.
# Pivot을 설정하고 리스트를 분할하는 방법에 따라 여러 방식으로 구분되는데, Hoare Partition 이 대표적.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # Return array if list contains less than 1 element
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# 전통 퀵 정렬의 분할 방식과는 조금 다른데, 피벗과 데이터를 비교하는 비교 연산 횟수가 증가하므로
# 시간 면에서는 조금 비효율적이다.

# # No List Comprehension
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#
#     pivot = array[0]
#     tail = array[1:]
#
#     left_side = []
#     right_side = []
#     for x in tail:
#         if x <= pivot:
#             left_side.append(x)
#         else:
#             right_side.append(x)
#
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#
#
# # Example usage:
# array = [3, 6, 8, 10, 1, 2, 1]
# print("Sorted array:", quick_sort(array))

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_longer(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]

    # Swap pivot into its correct position after pointers have crossed
    array[right], array[pivot] = array[pivot], array[right]

    quick_sort_longer(array, start, right - 1)
    quick_sort_longer(array, right + 1, end)

quick_sort_longer(array, 0, len(array) - 1)
print(array)

# 퀵 정렬의 시간 복잡도
# 선택 정렬과 삽입 정렬은 최악의 경우에도 항상 시간 복잡도 O(N^2) 을 보장하는 반면, 뷕 정렬의 평균 시간
# 복잡도는 O(NlogN) 이다. 앞서 다루었던 두 정렬 알고리즘에 비해 매운 빠른 편.
# 이유는 다른 정렬 방식들과 달리 N이 늘어날 수록 분할이 이루어지는 횟수가 기하급수적으로 감소하기 때문.


# 계수 정렬 (Count Sort)
# 계수 정렬 알고리즘은 특정한 조건이 부합할 때만 사용할 수 있지만, 매우 빠른 정렬 알고리즘이다.
# 모든 데이터가 양의 정수이고 데이터의 개수가 N 이며 데이터 중 최댓값이 K 일 때, 계수 정렬은
# 최악의 경우에도 수행 시간 O(N + K) 를 보장한다.

# 과정은 다음과 같다:

# Example
# Assume all elements >= 0
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# Initiate a list encompassing the entire range
count = [0] * (max(array) + 1)

# Update count
for i in range(len(array)):
    count[array[i]] += 1

# Visit each entry of count and print header as many times
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

# 계수 정렬의 시간 복잡도
# 모든 데이터가 양의 정수이고 데이터의 개수가 N 이며 데이터 중 최댓값이 K 일 때, 계수 정렬은
# 최악의 경우에도 수행 시간 O(N + K) 를 보장한다. 계수 정렬은 앞에서부터 데이터를 하나씩
# 확인하면서 리스트에서 적절한 인덱스의 값을 1씩 증가시킬 뿐만 아니라, 추후에 리스트의 각
# 인덱스에 해당하는 값들을 확인할 때 데이터 중 최댓값의 크기만큼 반복을 수행해야 하기 때문.
# 따라서 범위만 한정되어 있다면 효과적으로 사용할 수 있으며 항상 빠르게 동작한다. 사실상
# 현존하는 정렬 알고리즘 중에서 기수 정렬 (Radix Sort) 과 더불어 가장 빠르다 할 수 있다.

# 계수 정렬의 공간 복잡도
# 계수 정렬은 때에 따라 심각한 비효율성을 초래할 수 있다. 예를 들어 데이터가 0과 999,999,
# 단 2개만 존재한다 해도 리스트의 크기가 100만이 되도록 선언해야 함.또 다른 예로 성적의 경우
# 100점을 맞은 학생이 여럿일 수 있기에 계수 정렬이 효과적이다. 반면, 퀵 정렬은 일반적인 경우에
# 평균적으로 빨리 동작하기에 데이텅의 특성을 파악하기 어렵다면 퀵 정렬을 이용하는 것이 유리함.
# 다시 말해 계수 정렬은 데이터의 크기가 한정되어 있고, 데이터의 크기가 많이 중복되어 있을 수록 류이.


# 파이썬의 정렬 라이브러리
# 파이썬은 기본 정렬 라이브러리인 `sorted()` 함수를 제공한다. `sorted()` 는 퀵 정렬과 동작 방식이
# 비슷한 병합 정렬을 기반으로 만들어졌는데, 병합 정렬은 일반적으로 퀵 정렬보다 느리지만 최악의 경우에도
# 시간 복잡도 O(NlogN) 을 보장한다는 특징이 있다.

# Example 1
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

# Example 2
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)

# Example 3
# 리스트의 데이터가 튜플로 구성되어 있을 떄, 각 데이터의 두 번쨰 원소를 기준으로 설정
array = [('banana', 2), ('apple', 5), ('carrot', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)

# 정렬 라이브러리의 시간 복잡도
# 정렬 라이브러리는 최악의 경우에도 시간 복잡도 O(NlogN)을 보여주며, 퀵 정렬보다 효과적.
# 병합 정렬과 삽입 정렬의 하이브리드이며, 문제에서 별도의 요구 없이 단순히 정렬할 경우
# 기본 정렬 라이브러리를 이용하고, 데이터의 범위가 한정되어 있으며 빨라야 할 땐 계수 정렬.

# 결론:
# 1. 정렬 라이브러리로 풀 수 있는 문제:
# - 단순히 정렬 기법을 알고 있는지 물어보는 문제로 기본 정렬 라이브러리의 사용 방법을
#   숙지하고 있으면 어렵지 않게 풀 수 있다.
# 2. 정렬 알고리즘의 원리에 대해 물어보는 문제:
# - 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알고 있어야 문제를 풀 수 있다.
# 3. 더 빠른 정렬이 필요한 문제:
# - 퀵 정렬 기반의 정렬 기법으로는 풀 수 없으며 계수 정렬 등의 다른 정렬을 이용하거나
#   문제에서 알려진 알고리즘의 구조적인 개선을 거쳐야 풀 수 있다.
