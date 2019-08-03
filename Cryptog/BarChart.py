import matplotlib.pyplot as plt
import numpy as np
def showBarChart(inform = {}, name = "", N = 32):
    data = list(inform.values())
    labels = list(inform.keys())
    ind = np.arange(N)
    width = 0.5
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, data[0:N], width, color='r')
    ax.set_title(name)
    ax.set_xticks(ind)
    ax.set_xticklabels(labels[0:N])
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2, height, '%d' % int(height), ha='center', va='bottom')
    autolabel(rects1)
    plt.show()


