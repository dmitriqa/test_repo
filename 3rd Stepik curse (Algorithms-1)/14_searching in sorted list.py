def searching(n, left, right):
    global list_
    if left > right:
        return -1
    else:
        if n == list_[(left + right) // 2]:
            return (left + right) // 2 + 1
        elif n > list_[(left + right) // 2]:
            return searching(n, (left + right) // 2 + 1, right)
        elif n < list_[(left + right) // 2]:
            return searching(n, left, (left + right) // 2 - 1)


length_and_list = map(int, input().split())
length = next(length_and_list)
list_ = list(length_and_list)

to_search = map(int, input().split())
number = next(to_search)
to_search = list(to_search)

for i in to_search:
    print(searching(i, 0, len(list_) - 1), end= ' ')

"""двоичный поиск
﻿
В первой строке даны целое число n и массив A[] из n различных натуральных чисел в порядке возрастания, 
во второй — целое число k и k натуральных чисел 
Для каждого i от 1 до k необходимо вывести индекс j, для которого A[j] = b, или -1, если такого j нет.

Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11

Sample Output:
3 1 -1 1 -1
"""

