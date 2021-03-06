def moving_up(parent, child):
    global heap
    if heap[child] <= heap[parent]:
        pass
    else:
        heap[child], heap[parent] = heap[parent], heap[child]
        return moving_up(parent // 2, parent)


def moving_down(parent):
    global heap
    left_son = 2 * parent
    right_son = (2 * parent) + 1
    if len(heap) >= right_son + 1:
        if heap[parent] < max(heap[left_son], heap[right_son]):
            if heap[left_son] > heap[right_son]:
                heap[parent], heap[left_son] = heap[left_son], heap[parent]
                moving_down(left_son)
            else:
                heap[parent], heap[right_son] = heap[right_son], heap[parent]
                moving_down(right_son)
    elif len(heap) >= right_son and heap[parent] < heap[left_son]:
        heap[parent], heap[left_son] = heap[left_son], heap[parent]


heap = [float('inf')]
n = int(input())
for i in range(n):
    inf = input().split()
    if inf[0] == 'Insert':
        heap.append(int(inf[1]))
        moving_up((len(heap) - 1) // 2, len(heap) - 1)
    else:
        print(heap[1])
        if len(heap) > 2:
            a = heap.pop()
            heap[1] = a
            moving_down(1)
        else:
            a = heap.pop()

"""очередь с приоритетами

Первая строка входа содержит число операций n
Каждая из последующих n строк задают операцию одного из следующих двух типов:
Insert x, где 0 x — целое число;
ExtractMax.

Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.

Sample Input:
6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax

Sample Output:
200
500
"""