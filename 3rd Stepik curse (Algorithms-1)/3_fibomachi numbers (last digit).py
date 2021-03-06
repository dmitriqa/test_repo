def fib(n):
    counter = 2
    fib_numbers = [0, 1]
    while counter <= n:
        number = (fib_numbers[counter - 1] + fib_numbers[counter - 2]) % 10
        fib_numbers.append(number)
        counter += 1
    return fib_numbers[n]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()


"""Дано число n, 1≤n≤10^7
необходимо найти последнюю цифру n-го числа Фибоначчи.

Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно быть аккуратным с переполнением.
В данной задаче, впрочем, этой проблемы можно избежать, поскольку нас интересует только последняя цифра числа Фибоначчи:
если 0≤a,b≤9 — последние цифры чисел
соответственно, то (a+b) (a+b)mod10 — последняя цифра числа F_{i+2}

Sample Input:
696352
Sample Output:
9
"""