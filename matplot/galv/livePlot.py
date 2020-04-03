from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['aapl']
    y2 = data['amzn']
    y3 = data['sxtye']

    plt.cla()

    plt.plot(x, y1, label='AAPL')
    plt.plot(x, y2, label='AMZN')
    plt.plot(x, y3, label='SXTYE')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=10)

plt.tight_layout()
plt.show()
