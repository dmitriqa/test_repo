n = int(input())
D = [[float('inf'), float('inf')] for i in range(n + 1)]
D[1] = [0, float('inf')]
for number in range(2, n + 1):
    if number % 2 == 0:
        mult_2 = [D[number // 2][0] + 1, number / 2]
    else:
        mult_2 = [float('inf'), float('inf')]
    if number % 3 == 0:
        mult_3 = [D[number // 3][0] + 1, number / 3]
    else:
        mult_3 = [float('inf'), float('inf')]
    plus_1 = [D[number - 1][0] + 1, number - 1]
    D[number] = min(mult_2, mult_3, plus_1)
print(D[n][0])
ans = []
number = n
while number != float('inf'):
    ans.append(int(number))
    number = D[int(number)][1]
print(*reversed(ans))

"""калькулятор

У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом x: 
заменить x на 2x, 3x или x+1. По данному целому числу n определите минимальное число операций k,
необходимое, чтобы получить n из 1. Выведите k и последовательность промежуточных чисел.

Sample Input 1:
1
Sample Output 1:
0
1 
Sample Input 2:
5
Sample Output 2:
3
1 2 4 5 

Sample Input 3:
96234
Sample Output 3:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234 
"""