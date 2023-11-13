import matplotlib.pyplot as plt
import csv
from datetime import datetime

high = []
low = []
dates = []

with open('lect7\\3139529.csv') as csvf:
    reader = csv.reader(csvf)
    print(next(reader))

    for index, row in enumerate(reader):
        # print(index, row[2], row[5], row[6])
        if row[5] != '' and row[6] != '':
            dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
            if row[5] != '':
                high.append(float(row[5]))
            if row[6] != '':
                low.append(float(row[6]))
# print(high)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
fig.autofmt_xdate()
ax.plot(dates, high, c='red')
ax.plot(dates, low)
ax.set_title('Temperature in Sofia', fontsize=20)
ax.set_xlabel('Dates', fontsize=14)
ax.set_ylabel('Temp(C)', fontsize=14)

plt.show()
