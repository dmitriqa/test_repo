def LIS_BottomUp(array):
    D = [1 for i in range(len(array))]
    for i in range(len(array)):
        for j in range(i):
            if array[i] % array[j] == 0 and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    return max(D)


def main():
    n = int(input())
    array = list(map(int, input().split()))
    print(LIS_BottomUp(array))


if __name__ == "__main__":
    main()

"""наибольшая последовательнократная подпоследовательность

Дано целое число n и массив A[1…n] натуральных чисел. Выведите максимальное 1≤k≤n, для которого найдётся 
подпоследовательность 1≤i(1)≤i(2)...≤i(k)≤n длины k, в которой каждый элемент делится на предыдущий 

Sample Input:
4
3 6 7 12

Sample Output:
3
"""