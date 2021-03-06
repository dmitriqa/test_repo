string = list(input())
queue = []
# queue2 = []
for i in set(string):
    queue.append((i, string.count(i)))
queue.sort(key=lambda x: x[1], reverse=True)
if len(queue) == 1:
    print('1', len(string))
    print(string[0] + ': 0')
    print('0' * len(string))
else:
    dict= {}
    for i in range(len(queue) -1):
        dict[queue[i][0]] = '1' * i + '0'
    dict[queue[-1][0]] = '1' * (len(queue) - 1)
    ans = ''
    for letter in string:
        ans += dict[letter]
    print(len(queue), len(ans))
    for key, value in dict. items():
        print(key + ': ' + value)
    print(ans)
# while len(queue) > 1:
#     print(queue)
#     i = queue.pop()
#     j = queue.pop()
#     queue2.append(i)
#     queue2.append(j)
#     queue.append((i[0] + j[0], i[1] + j[1]))
