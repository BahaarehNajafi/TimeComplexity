import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time


def bubble_sort(the_list):
    for i in range(len(the_list) - 1, 0, -1):
        for j in range(i):
            if the_list[j] > the_list[j + 1]:
                temp = the_list[j]
                the_list[j] = the_list[j + 1]
                the_list[j + 1] = temp
    return the_list


def binary_search(the_list, item):
    first = 0
    last = len(the_list) - 1
    while first <= last:
        mid = int((last + first) / 2)
        if the_list[mid] == item:
            return
        else:
            if item < the_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return


def hanoi(N, A, B, C):
    if N == 1:
        return
        # print("move disk", N, "from", A, "to", C)
    else:
        hanoi(N - 1, A, C, B)
        # print("move disk", N, "from", A, "to", C)
        hanoi(N - 1, B, A, C)


def linear_search(the_list, item):
    for i in the_list:
        if i == item:
            return
    else:
        return


def quick_sort(the_list):
    less = []
    pivot_list = []
    more = []
    if len(the_list) <= 1:
        return the_list
    else:
        pivot = the_list[0]
        for i in the_list:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_list.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivot_list + more


def merge_sort(the_list):
    if len(the_list) > 1:
        mid = len(the_list) // 2
        left_half = the_list[:mid]
        right_half = the_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                the_list[k] = left_half[i]
                i += 1

            else:
                the_list[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):
            the_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            the_list[k] = right_half[j]
            j += 1
            k += 1


def siftdown(the_list, start, end):
    while True:
        child = start * 2 + 1
        if child > end:
            break
        if child + 1 <= end and the_list[child] < the_list[child + 1]:
            child += 1
        if the_list[start] < the_list[child]:
            the_list[start], the_list[child] = the_list[child], the_list[start]
            start = child
        else:
            break


def heap_sort(the_list):
    for start in range((len(the_list) - 2) // 2, -1, -1):
        siftdown(the_list, start, len(the_list) - 1)

    for end in range(len(the_list) - 1, 0, -1):
        the_list[end], the_list[0] = the_list[0], the_list[end]
        siftdown(the_list, 0, end - 1)
    return the_list


print('1. bubble sort\n2. binary search\n3. hanoi towers\n4. linear search\n5. quick sort\n6. merge sort\n7. heap sort')
inp = int(input("enter your choice: "))

nl = list()
tm = list()
the_label = ''

# bubble sort
if inp == 1:
    the_label = mpatches.Patch(label='time complexity for bubble sort')
    for i in range(1, 10):
        n = 1000 * i
        random_list = list(range(1, n))
        reversed(random_list)  # reversing the list so we have the worst case
        t1 = time.clock()
        bubble_sort(random_list)
        t2 = time.clock()
        nl.append(n)
        tm.append(t2 - t1)

# binary search
if inp == 2:
    the_label = mpatches.Patch(label='time complexity for binary search')
    for i in range(1, 10):
        n = 1000000 * i
        random_list = list(range(1, n))
        t1 = time.clock()
        binary_search(random_list, 0)  # searching an item that does not exist, for worst case
        t2 = time.clock()
        nl.append(n)
        tm.append(t2 - t1)

# hanoi towers
if inp == 3:
    the_label = mpatches.Patch(label='time complexity for hanoi')
    for i in range(1, 10):
        n = 1 * i

        t1 = time.clock()
        hanoi(n, 'a', 'b', 'c')
        t2 = time.clock()

        nl.append(n)
        tm.append(t2 - t1)

# linear search
if inp == 4:
    the_label = mpatches.Patch(label='time complexity for linear search')
    for i in range(1, 10):
        n = 100000 * i
        random_list = list(range(1, n))
        t1 = time.clock()
        linear_search(random_list, 0)
        t2 = time.clock()

        nl.append(n)
        tm.append(t2 - t1)

# quick sort
if inp == 5:
    the_label = mpatches.Patch(label='time complexity for quick sort')
    for i in range(1, 10):
        n = 100000 * i
        random_list = list(range(1, n))
        reversed(random_list)

        t1 = time.clock()
        quick_sort(random_list)
        t2 = time.clock()

        nl.append(n)
        tm.append(t2 - t1)

# merge sort
if inp == 6:
    the_label = mpatches.Patch(label='time complexity for merge sort')
    for i in range(1, 10):
        n = 100000 * i
        random_list = list(range(1, n))
        reversed(random_list)

        t1 = time.clock()
        merge_sort(random_list)
        t2 = time.clock()

        nl.append(n)
        tm.append(t2 - t1)

# heap sort
if inp == 7:
    the_label = mpatches.Patch(label='time complexity for heap sort')
    for i in range(1, 10):
        n = 100000 * i
        random_list = list(range(1, n))
        reversed(random_list)

        t1 = time.clock()
        heap_sort(random_list)
        t2 = time.clock()

        nl.append(n)
        tm.append(t2 - t1)


plt.plot(nl, tm)
plt.legend(handles=[the_label])
plt.xlabel('length of the lists')
plt.ylabel('time', multialignment='center')
plt.show()
