n = int(input())
summand = 1
all_summands = []
sum = 0
while sum + summand + summand + 1 <= n:
    sum += summand
    all_summands.append(summand)
    summand += 1
all_summands.append(n - sum)
print(len(all_summands))
print(*all_summands)

"""различные слагаемые
По данному числу n найдите максимальное число k, для которого n можно представить как сумму k различных
 натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых.

Sample Input 1:
4
Sample Output 1:
2
1 3 

Sample Input 2:
6
Sample Output 2:
3
1 2 3
"""