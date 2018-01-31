import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time


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


nl = list()
tm = list()
for i in range(1, 10):
    n = 100000 * i
    random_list = list(range(1, n))
    reversed(random_list)  # for worst case result, we revers the list

    t1 = time.clock()
    quick_sort(random_list)
    t2 = time.clock()

    nl.append(n)
    tm.append(t2 - t1)

plt.plot(nl, tm)
the_label = mpatches.Patch(label='time complexity for quick sort')
plt.legend(handles=[the_label])
plt.xlabel('length of the lists')
plt.ylabel('time', multialignment='center')
plt.show()
