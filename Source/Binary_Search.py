import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time


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


nl = list()
tm = list()
for i in range(1, 10):
    n = 10000 * i
    random_list = list(range(1, n))
    t1 = time.clock()
    binary_search(random_list, 0)  # to show the worst case result, we search something that is not the list
    t2 = time.clock()
    nl.append(n)
    tm.append(t2 - t1)

plt.plot(nl, tm)
the_label = mpatches.Patch(label='time complexity for binary search')
plt.legend(handles=[the_label])
plt.xlabel('length of the lists')
plt.ylabel('time', multialignment='center')
plt.show()
