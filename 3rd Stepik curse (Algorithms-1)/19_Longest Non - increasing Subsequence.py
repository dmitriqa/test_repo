n = int(input())
array = list(map(int, input().split()))
p = [0] * n
m = [0] * (n + 1)
l = 0
array = array[::-1]
for i in range(n):
    low = 1
    high = l
    while low <= high:
        mid = (low + high) // 2
        if array[m[mid]] < array[i]:
            low = mid + 1
        elif array[m[mid]] == array[i]:
            low += 1
        else:
            high = mid - 1
    new_L = low
    p[i] = m[new_L - 1]
    if new_L > l:
        m[new_L] = i
        l = new_L
    elif array[i] < array[m[new_L]]:
        m[new_L] = i
reverse = []
k = m[l]
for i in range(l - 1, -1, -1):
    reverse.append(n - k)
    k = p[k]
print(len(reverse))
print(*reverse)

"""Задача на программирование повышенной сложности: наибольшая невозрастающая подпоследовательность

Дано целое число n и массив A[1…n], содержащий неотрицательные целые числа. 
Найдите наибольшую невозрастающую подпоследовательность в A. В первой строке выведите её длину k, 
во второй — её индексы 1≤i(1)<i(2)<…<i(k)≤n (таким образом, A[i(1)]≥A[i(2)]≥…≥A[i(n)]).

Sample Input:
5
5 3 4 4 2

Sample Output:
4
1 3 4 5 
"""
