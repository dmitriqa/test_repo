def pizano_period(n, m):
    counter = 1
    cycle = [0, 1]
    while 1:
        cycle.append((cycle[-2] + cycle[-1]) % m)
        if cycle[-2] == 0 and cycle[-1] == 1:
            break
        counter += 1
        if counter > 150000:
            return cycle[n % m]
    # print(cycle)
    position = n % (len(cycle) - 2)
    return cycle[position]


def main():
    n, m = (int(i) for i in input().split())
    print(pizano_period(n, m))


if __name__ == "__main__":
    main()

"""Задача на программирование повышенной сложности: огромное число Фибоначчи по модулю

Даны целые числа 1 ≤n≤ 10^18
  и 2 ≤m≤ 10^5
необходимо найти остаток от деления nn-го числа Фибоначчи на mm.

Sample Input:
10 2
Sample Output:
1
"""