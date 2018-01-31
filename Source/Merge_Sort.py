import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time



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


nl = list()
tm = list()
for i in range(1, 10):
    n = 100000 * i
    random_list = list(range(1, n))
    reversed(random_list)  # for worst case result, we revers the list

    t1 = time.clock()
    merge_sort(random_list)
    t2 = time.clock()

    nl.append(n)
    tm.append(t2 - t1)

plt.plot(nl, tm)
the_label = mpatches.Patch(label='time complexity for merge sort')
plt.legend(handles=[the_label])
plt.xlabel('length of the lists')
plt.ylabel('time', multialignment='center')
plt.show()
