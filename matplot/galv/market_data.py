import random
import csv
import time


x_value = 0
aapl = 250
amzn = 350
sxtye = 400

fieldnames = ['x_value', 'aapl', 'amzn', 'sxtye']

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()


while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            'x_value': x_value,
            'aapl': aapl,
            'amzn': amzn,
            'sxtye': sxtye
        }

        csv_writer.writerow(info)
        print(x_value, aapl, amzn, sxtye)

        x_value += 1
        aapl = aapl + random.randint(-6, 8)
        amzn = amzn + random.randint(-4, 5)
        sxtye = sxtye + random.randint(-2, 9)

    time.sleep(.1)

