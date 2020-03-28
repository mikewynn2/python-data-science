# import csv
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
# for row in csv_reader:
    # lang_counter.update(row['LanguagesWorkedWith'].split(';'))

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

lang_counter = Counter()

for response in lang_responses:
    lang_counter.update(response.split(';'))

langs = []
popularity = []

for item in lang_counter.most_common(20):
    langs.append(item[0])
    popularity.append(item[1])

langs.reverse()
popularity.reverse()
plt.barh(langs, popularity)
plt.title('Most Popular Languages')
# plt.ylabel('Languages')
plt.xlabel('Users')
plt.tight_layout()

plt.show()
