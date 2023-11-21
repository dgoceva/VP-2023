import matplotlib.pyplot as plt
import csv
from datetime import datetime

highs = []
lows = []
dates = []

with open('lect7\\3139529.csv') as csvf:
    reader = csv.reader(csvf)
    print(next(reader))

    for index, row in enumerate(reader):
        try:
            high = float(row[5])
            low = float(row[6])
        except ValueError:
            # print('No valid high or low temperature')
            pass
        else:
            dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
            highs.append(high)
            lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
fig.autofmt_xdate()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.set_title('Temperature in Sofia', fontsize=20)
ax.set_xlabel('Dates', fontsize=14)
ax.set_ylabel('Temp(C)', fontsize=14)

plt.show()
