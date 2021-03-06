W, n = map(int, input().split())
weights = list(map(int, input().split()))
D = [[float('inf') for i in range(n + 1)] for j in range(W + 1)]
for w in range(W + 1):
    D[w][0] = 0
for i in range(n + 1):
    D[0][i] = 0
for i in range(1, n + 1):
    for w in range(1, W + 1):
        D[w][i] = D[w][i - 1]
        if weights[i - 1] <= w:
            D[w][i] = max(D[w][i], D[w - weights[i - 1]][i - 1] + weights[i - 1])
print(D[W][n])

"""рюкзак

Первая строка входа содержит целые числа W и n — вместимость рюкзака и число золотых слитков. 
Следующая строка содержит n целых чисел w(1) - w(n), задающих веса слитков. Найдите максимальный вес золота, 
который можно унести в рюкзаке.

Sample Input:
10 3
1 4 8
Sample Output:
9
"""