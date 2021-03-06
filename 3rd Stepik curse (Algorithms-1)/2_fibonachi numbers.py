def fib(n):
    counter = 2
    fib_numbers = [0, 1]
    while counter <= n:
        number = fib_numbers[counter - 1] + fib_numbers[counter - 2]
        fib_numbers.append(number)
        counter += 1
    return fib_numbers[n]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()


"""Дано целое число n 1≤n≤40, необходимо вычислить n-е число Фибоначчи

Sample Input:

3
Sample Output:

2
"""