n = int(input())
numbers = list(map(int, input().split()))
dict = [0 for i in range(11)]
for number in numbers:
    dict[number] += 1
for number in range(len(dict)):
    if dict[number] != 0:
        print(((str(number) + ' ') * dict[number]), end='')

"""сортировка подсчётом 

Первая строка содержит число n, вторая — n натуральных чисел, не превышающих 10. 
Выведите упорядоченную по неубыванию последовательность этих чисел.
"""