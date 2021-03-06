n, length = map(int, input().split())
dict = []
for i in range(n):
    dict.append((input().split(': ')))
string = input()
symbols = ''
ans = ''
for symbol in string:
    symbols += symbol
    for element in dict:
        if symbols == element[1]:
            ans += element[0]
            symbols = ''
print(ans)
