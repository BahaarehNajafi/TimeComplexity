import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time



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
    return


nl = list()
tm = list()
for i in range(1, 10):
    n = 100000 * i
    random_list = list(range(1, n))
    reversed(random_list)  # for worst case result, we revers the list

    t1 = time.clock()
    heap_sort(random_list)
    t2 = time.clock()

    nl.append(n)
    tm.append(t2 - t1)

plt.plot(nl, tm)
the_label = mpatches.Patch(label='time complexity for heap sort')
plt.legend(handles=[the_label])
plt.xlabel('length of the lists')
plt.ylabel('time', multialignment='center')
plt.show()
