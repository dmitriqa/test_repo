def quick_sort(l, r, zero_or_one):
    global sections
    while l < r:
        n, m = partition(l, r, zero_or_one)
        # if zero_or_one == 1:
        #     print(n, m)
        #     print(sections)
        quick_sort(l, n - 1, zero_or_one)
        l = m + 1


def partition(l, r, zero_or_one):
    global sections
    # sections[l], sections[(l + r) // 2 - 2] = sections[(l + r) // 2 - 2], sections[l]
    x = sections[l][zero_or_one]
    j = l
    for i in range(l + 1, r + 1):
        if sections[i][zero_or_one] <= x:
            j += 1
            sections[j], sections[i] = sections[i], sections[j]
    # print(sections, '!', l, r)
    r = 0
    r += j
    j = l
    for i in range(l, r):
        if sections[i][zero_or_one] < x:
            j += 1
            sections[j], sections[i] = sections[i], sections[j]
    sections[j], sections[l] = sections[l], sections[j]
    return j, r


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
        elif n >= sections[(left + right) // 2 + 1][1]:
            return finished(n, (left + right) // 2, right)
        elif n <= sections[(left + right) // 2][1]:
            return finished(n, left, (left + right) // 2)

n, m = map(int, input().split())
sections = []
for i in range(n):
    sections.append(tuple(map(int, input().split())))
points = list(map(int, input().split()))
len_sections = len(sections)
quick_sort(0, len_sections - 1, 0)
left_sections = []
for section in sections:
    left_sections.append(section)
quick_sort(0, len_sections - 1, 1)
print(left_sections)
print(sections)
for point in points:
    print(began(point, 0, len_sections - 1), finished(point, 0, len_sections - 1), end=' ')
