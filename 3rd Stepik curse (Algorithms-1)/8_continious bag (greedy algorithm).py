n, W = map(int, input().split(' '))
things = []
for i in range(n):
    things.append(tuple(map(int, input().split())))
things.sort(key=lambda x: x[0] / x[1])
things = reversed(things)
sum = 0
for thing in things:
    sum += thing[0] * min((W / thing[1], 1))
    W -= thing[1] * min((W / thing[1], 1))
print(sum)

"""непрерывный рюкзак

Первая строка содержит количество предметов n и вместимость рюкзака W
Каждая из следующих nn строк задаёт стоимость c и w предмета (n, W, c, w — целые числа).
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, 
стоимость и объём при этом пропорционально уменьшатся), 
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:
3 50
60 20
100 50
120 30
Sample Output:
180.000
"""