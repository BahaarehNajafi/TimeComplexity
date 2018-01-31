import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time


def linear_search(the_list, item):
    for i in the_list:
        if i == item:
            print(item, "was found!")
    else:
        return


nl = list()
tm = list()
for i in range(1, 10):
    n = 100000 * i
    random_list = list(range(1, n))
    t1 = time.clock()
    linear_search(random_list, 0)  # to show the worst case result, we search something that is not the list
    t2 = time.clock()
    nl.append(n)
    tm.append(t2 - t1)

plt.plot(nl, tm)
the_label = mpatches.Patch(label='time complexity for linear search')
plt.legend(handles=[the_label])
plt.xlabel('length of the lists')
plt.ylabel('time', multialignment='center')
plt.show()

