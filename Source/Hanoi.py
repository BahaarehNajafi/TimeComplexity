import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import time


def hanoi(N, A, B, C):
    if N == 1:
        return
        # print("move disk", N, "from", A, "to", C)
    else:
        hanoi(N - 1, A, C, B)
        # print("move disk", N, "from", A, "to", C)
        hanoi(N - 1, B, A, C)


nl = list()
tm = list()
for i in range(1, 10):
    n = 1 * i

    t1 = time.clock()
    hanoi(n, 'a', 'b', 'c')
    t2 = time.clock()

    nl.append(n)
    tm.append(t2 - t1)

plt.plot(nl, tm)
the_label = mpatches.Patch(label='time complexity for hanoi')
plt.legend(handles=[the_label])
plt.xlabel('length of the lists')
plt.ylabel('time', multialignment='center')
plt.show()
