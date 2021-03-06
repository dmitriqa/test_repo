def began(n, left, right):
    global len_sections
    global left_sections
    if n < left_sections[0][0]:
        return 0
    elif n >= left_sections[-1][0]:
        return len_sections
    else:
        # print((left + right) // 2, (left + right) // 2 + 1)
        if left_sections[(left + right) // 2][0] <= n < left_sections[(left + right) // 2 + 1][0]:
            return (left + right) // 2 + 1
        elif n >= left_sections[(left + right) // 2 + 1][0]:
            return began(n, (left + right) // 2, right)
        elif n < left_sections[(left + right) // 2][0]:
            return began(n, left, (left + right) // 2)


def finished(n, left, right):
    global len_sections
    global sections
    if n <= sections[0][1]:
        return 0
    elif n > sections[-1][1]:
        return len_sections
    else:
        # print((left + right) // 2, (left + right) // 2 + 1)
        if sections[(left + right) // 2][1] < n <= sections[(left + right) // 2 + 1][1]:
            return (left + right) // 2 + 1
        elif n <= sections[(left + right) // 2][1]:
            return finished(n, left, (left + right) // 2)
        elif n > sections[(left + right) // 2 + 1][1]:
            return finished(n, (left + right) // 2, right)

n, m = map(int, input().split())
sections = []
left_sections = []
for i in range(n):
    sections.append(tuple(map(int, input().split())))
points = list(map(int, input().split()))
len_sections = len(sections)
for i in sections:
    left_sections.append(i)
left_sections.sort()
sections.sort(key=lambda x: x[1])
for point in points:
    print(began(point, 0, len_sections - 1) - finished(point, 0, len_sections - 1), end=' ')

"""точки и отрезки

В первой строке задано два целых числа n, m — количество отрезков и точек на прямой, соответственно. 
Следующие n строк содержат по два целых числа a(i) и b(i), (a(i) <= b(i)) — координаты концов отрезков. 
Последняя строка содержит m целых чисел — координаты точек. Точка считается принадлежащей отрезку, если она находится 
внутри него или на границе. Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.

Sample Input:
2 3
0 5
7 10
1 6 11

Sample Output:
1 0 0
"""