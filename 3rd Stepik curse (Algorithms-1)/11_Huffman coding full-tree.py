def coding_symbols(tree, coded):
    global dict
    if len(tree) > 1:
        return coding_symbols(tree[0], coded + '0'), coding_symbols(tree[1], coded + '1')
    else:
        dict[tree] = coded
        return tree, coded


string = list(input())
queue = []
dict = {}
for i in set(string):
    queue.append((i, string.count(i)))
if len(queue) == 1:
    print('1', len(string))
    print(string[0] + ': 0')
    print('0' * len(string))
else:
    for k in range(len(queue) -1):
        queue.sort(key=lambda x: x[1], reverse=True)
        i = queue.pop()
        j = queue.pop()
        queue.append(((i[0], j[0]), i[1] + j[1]))
    coding_symbols(queue[0][0], '')
    ans = ''
    for letter in string:
        ans += dict[letter]
    print(len(dict), len(ans))
    for key, value in dict. items():
        print(key + ': ' + value)
    print(ans)

"""кодирование Хаффмана

По данной непустой строке s, состоящей из строчных букв латинского алфавита, 
постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k, 
встречающихся в строке, и размер получившейся закодированной строки. В следующих k строках запишите коды букв 
в формате "letter: code". В последней строке выведите закодированную строку.

Sample Input 1:
a
Sample Output 1:
1 1
a: 0
0

Sample Input 2:
abacabad
Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
"""