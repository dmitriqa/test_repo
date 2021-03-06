string1 = input()
string2 = input()
n = len(string1)
m = len(string2)
D = [[float('inf') for i in range(n + 1)] for j in range(m + 1)]
for i in range(n + 1):
    D[0][i] = i
for j in range(m + 1):
    D[j][0] = j
for i in range(1, n + 1):
    for j in range(1, m + 1):
        c = 1
        if string1[i - 1] == string2[j - 1]:
            c = 0
        D[j][i] = min(D[j - 1][i] + 1, D[j][i - 1] + 1, D[j - 1][i - 1] + c)
print(D[m][n])

"""расстояние редактирования

Вычислите расстояние редактирования двух данных непустых строк, содержащих строчные буквы латинского алфавита.

Sample Input 1:
ab
ab
Sample Output 1:
0

Sample Input 2:
short
ports
Sample Output 2:
3
"""