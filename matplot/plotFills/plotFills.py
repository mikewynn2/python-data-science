import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')
plt.plot(ages, js_salaries, label='JS')

# overall_median = 57287

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries > dev_salaries),
                 interpolate=True, color='blue', alpha=0.25, label='Above Avg')

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries <= dev_salaries),
                 interpolate=True, color='red', alpha=0.25, label='Below Avg')

plt.fill_between(ages, js_salaries, dev_salaries,
                 where=(js_salaries > dev_salaries),
                 interpolate=True, color='green', alpha=0.25, label='js Above Avg')

plt.fill_between(ages, js_salaries, dev_salaries,
                 where=(js_salaries <= dev_salaries),
                 interpolate=True, color='orange', alpha=0.25, label='js Below Avg')
plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()
