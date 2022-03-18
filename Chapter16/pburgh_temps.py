import csv
import matplotlib.pyplot as plt
from datetime import datetime

dates=[]
highs = []
lows = []

with open('data/pittsburgh.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header_row = next(csv_reader)
    for row in csv_reader:
        date = datetime.strptime(row[2], '%Y-%m-%d') 
        try: 
            high=int(row[3])
            low=int(row[4])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

plt.scatter(dates,highs,c="red", label='highs')
plt.scatter(dates,lows,c="blue", label='lows')
plt.ylabel('Temperature (Degrees F)')
plt.xlabel('Date')
plt.title('Pittsburgh Temps (Jan - Mar 2022)')
plt.grid()
plt.show()