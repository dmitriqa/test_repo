def LIS_BottomUp(array):
    D = [1 for i in range(len(array))]
    I = [-1 for i in range(len(array))]
    for i in range(len(array)):
        for j in range(i):
            if array[j] >= array[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
                I[i] = j
    return D, I, max(D)

def finding_all_LIS(D, I, maxD, array):
    ans = []
    i = D.index(maxD)
    while i != -1:
        ans.append(i + 1)
        i = I[i]
    return list(reversed(ans))


def main():
    n = int(input())
    array = list(map(int, input().split()))
    D, I, maxD = LIS_BottomUp(array)
    ans = finding_all_LIS(D, I, maxD, array)
    print(maxD)
    print(*ans)


if __name__ == "__main__":
    main()