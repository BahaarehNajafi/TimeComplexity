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


nl = list()
tm = list()
for i in range(1, 10):
    n = 1000 * i
    random_list = list(range(1, n))
    reversed(random_list)  # for worst case result, we revers the list

    t1 = time.clock()
    bubble_sort(random_list)
    t2 = time.clock()

    nl.append(n)
    tm.append(t2 - t1)

plt.plot(nl, tm)
the_label = mpatches.Patch(label='time complexity for bubble sort')
plt.legend(handles=[the_label])
plt.xlabel('length of the lists')
plt.ylabel('time', multialignment='center')
plt.show()
