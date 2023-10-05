#1 당장 좋은 것만 선택하는 그리디

# 그리디 알고리즘은 어떠한 문제가 있을 때 단순 무식하게, 탐욕적으로 현재 상황에서
# 지금 당장 좋은 것만 고르는 방법을 의미한다.

# 코딩 테스트에서 접할 그리디 알고리즘의 문제 유형은 '사전에 외우고 있지 않아도
# 풀 수 있을 가능성이 높은 문제 유형' 이라는 특징이 있다.

# 예를 들어 여러 개의 데이터를 빠르게 정렬해야 하는 문제는 정렬 라이브러리를,
# 최단 경로를 빠르게 찾아야 하는 문제는 플로이드 워셜 (Floyd-Warshall) 혹은
# 다익스트라 (Dijkstra) 알고리즘을 외워 사용해야 한다.

# 보통 코딩 테스트에서 출제되는 그리디 알고리즘 유형의 문제는 창의력, 즉 문제를 풀기 위한
# 최소한의 아이디어를 떠올릴 수 있는 능력을 요구한다.

# 그리디 알고리즘은 어떠한 기준에 따라 가장 좋은 것을 선택하는 알고리즘이므로 문제에서
# "가장 큰 순서대로", "가장 작은 순서대로" 와 같은 기준을 알게 모르게 제시해준다.

# 대체로 이 기준은 정렬 알고리즘을 사용했을 때 만족시킬 수 있으므로 그리디 알고리즘 문제는
# 자주 정렬 알고리즘과 짝을 이뤄 출제된다.

# 예제 3-1: 거스름돈
# 당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원,
# 50원, 10원짜리 동전이 무한히 존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러
# 줘야 할 동정의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

# 전략: 가장 큰 화폐 단위부터 돈을 거슬러 준다

N = int(input())
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count = count + (N // coin)
    N = N % coin

print(count)

# 그리디 알고리즘의 정당성:
# 그리디 알고리즘은 탐욕적으로 문제에 접근했을 때 정확한 답을 찾을 수 있다는 보장이 있을 때 유용하다.
# 그리디 알고리즘으로 문제의 해버블 찾았을 때는 그 해법이 정당한지 검토해야 한다.
# 거스름돈 문재를 그리디 알고리즘으로 해결할 수 있는 이유는 가지고 있는 동전 중에서 큰 단위가 항상
# 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문이다.
# 만약 [500, 400, 100]: 800 = 400 + 400 // 500 + 100 + 100 + 100

# 결론: 그리디 알고리즘 문제에서는 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지
# 검토할 수 있어야 답을 도출할 수 있다.

# 어떤 코딩 테스트 문제를 만났을 때, 바로 문제 유형을 파악하기 어렵다면 그리디 알고리즘을 의심하고
# 문제를 해결할 수 있는 탐욕적인 해결법이 존재하는지 고민해보고 불가하다면 다이나믹 프로그래밍이나
# 그래프 알고리즘 등으로 해결할 수 있는지를 재차 고민해보는 것도 한 방법이다.

# 예제 3-2: 큰 수의 법칙

# 문제: 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는데
#      같은 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 특징이다

# 예:  n, m, k = 5, 8, 3
#     data = [2, 4, 5, 4, 6]
#     output: 46

# 전략:
# 1. Receive ints n, m, k separated by spaces
# 2. Receive a list of ints
# 3. Sort data from largest to smallest
# 4. Define the largest two ints
# 5. Add the largest int 'k' times using for loop
# 6. When m = 0, break the loop
# 7. If m = 0 after the loop, break while loop
# 7. When the loop is done, add second largest once
# 8. Decrease m by 1

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

sum = 0

data.sort()
first = data[n-1]
second = data[n-2]

while True:
    for i in range(k):
        if m==0:
            break
        sum += first
        m -= 1
    if m == 0:
        break
    sum += second
    m -= 1

print(sum)

# Input:
# 5 8 3
# 2 4 5 4 6

# Output:
# 46

# Alternate (Better) Method:
# Calculate the number of times that the largest is added

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k + 1)) * k + (m % (k + 1))

sum = 0
sum += count * first
sum += (m - count) * second

print(sum)

# 예제 3-3: 숫자 카드 게임
# 문제: N x M 행렬로 놓아진 카드들 중 다음과 같은 룰에 따라 가장 큰 한 숫자를 뽑는다
# 1. 뽑고자 하는 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 2. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑는다.
# 3. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를
#    뽑을 걳을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세운다.

# 전략:
# 1. Get integers N, M and each row
# 2. Iterate through each row and find the min
# 3. Find the largest minimum value

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    minVal = min(data)
    result = max(result, minVal)

print(result)

# Input:
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# Output:
# 2

# 예제 3-4: 1이 될 때까지
# 문제: 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선책하여 수행하려고 한다.
#      단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
#      1. N에서 1을 뺀다.
#      2. N을 K로 나눈다.

# 전략:
# 1. Receive ints k and n & set a counter = 0
# 2. Use a while loop (while True, continue computation, break if N = 1)
# 3. Use if statement to see if N is divisible by K (N % K = 0)
# 4. If so, divide N by K and increase counter by 1
# 5. Elif, subtract N by 1 and increase counter by 1
# 6. When the while loop breaks, print counter

# 내 답안
n, k = map(int, input().split())
counter = 0

while True:
    if n == 1:
        break
    elif n % k == 0:
        n = n / k
        counter += 1
    else:
        n -= 1
        counter += 1

print(counter)

# 모범답안
n, k = map(int, input().split())
counter = 0

while n >= k:
    while n % k != 0:
        n -= 1
        counter += 1
        n //= k
        counter += 1

while n > 1:
    n -= 1
    result += 1

print(result)

# While both of these answers make sense, they are not really scalable.
# It is better to subtract in chunk until N becomes a multiple of K

n, k = map(int, input().split())
counter = 0

while True:
    # Subtract 1 until N is K's multiple
    target = (n // k) * k
    n = target
    counter += (n - target)
    # ---- treat as a separate loop
    # Escape when N is not divisible anymore
    if n < k:
        break
    # divide by K
    n //= k
    counter += 1

counter += (n - 1)
print(counter)