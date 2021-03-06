def merge(A, B):
    global inversion_counter
    C = []
    i = 0
    j = 0
    len_A = len(A)
    len_B = len(B)
    while i < len_A and j < len_B:
        if B[j] < A[i]:
            inversion_counter += len_A - i
            C.append(B[j])
            j += 1
        else:
            C.append(A[i])
            i += 1
    if len_A == i:
        for el in B[j:]:
            C.append(el)
    else:
        for el in A[i:]:
            C.append(el)
    return C


n = int(input())
inf = list(map(int, input().split()))
queue = []
for i in range(n):
    queue.append([inf[i]])
inversion_counter = float(0)

while len(queue) > 1:
    queue2 = []
    for k in range(len(queue) // 2):
        queue2.append(merge(queue[2 * k], queue[2 * k + 1]))
    if len(queue) % 2 == 1:
        queue2.append(queue[-1])
    queue = queue2

print(int(inversion_counter))

"""число инверсий
﻿
Первая строка содержит число n, вторая — массив A[1…n], содержащий натуральные числа. Необходимо 
посчитать число пар индексов 1 ≤ i < j ≤ n, для которых A[i]>A[j]. (Такая пара элементов называется инверсией массива. 
Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: например, 
в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию, 
инверсию образуют каждые два элемента.)

Sample Input:
5
2 3 9 2 9

Sample Output:
2
"""
