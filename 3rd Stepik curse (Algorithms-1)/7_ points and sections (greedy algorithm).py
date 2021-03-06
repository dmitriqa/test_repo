sections = []
n = int(input())
for i in range(n):
    sections.append(tuple(map(int, input().split(' '))))
sections.sort(key=lambda x: x[1])
ans = [-1]
for section in sections:
    if ans[-1] < section[0]:
        ans.append(section[1])
print(len(ans) - 1)
print(*ans[1:])

"""покрыть отрезки точками

По данным n отрезкам необходимо найти множество точек минимального размера, 
для которого каждый из отрезков содержит хотя бы одну из точек.
В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит по два числа,
задающих начало и конец отрезка. Выведите оптимальное число mm точек и сами mm точек. 
Если таких множеств точек несколько, выведите любое из них.

Sample Input 1:
3
1 3
2 5
3 6
Sample Output 1:
1
3 

Sample Input 2:
4
4 7
1 3
2 5
5 6
Sample Output 2:
2
3 6 
"""