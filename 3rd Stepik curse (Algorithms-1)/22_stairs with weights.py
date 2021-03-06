n = int(input())
weights = [0] + list(map(int, input().split()))
D = [float('-inf') for i in range(n + 1)]
for i in range(n + 1):
    if i <= 1:
        D[i] = weights[i]
    else:
        D[i] = max(D[i-2], D[i-1]) + weights[i]
print(D[n])

"""лестница

Даны число n ступенек лестницы и целые числа a(1)...a(n), которыми помечены ступеньки. Найдите максимальную сумму, 
которую можно получить, идя по лестнице снизу вверх (от нулевой до n-й ступеньки), 
каждый раз поднимаясь на одну или две ступеньки.

Sample Input 1:
2
1 2
Sample Output 1:
3

Sample Input 2:
2
2 -1
Sample Output 2:
1

Sample Input 3:
3
-1 2 1
Sample Output 3:
3
"""