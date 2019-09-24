import csv
from matplotlib import pyplot as plt
from datetime import datetime

#Pobranie z pliku dat oraz najwyższych i najniższych temperatur w poszczególnych dniach.
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        low = int(row[6])
        lows.append(low)

        high = int(row[5])
        highs.append(high)

    print(highs)

#Dane wykresu
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Formatowanie wykresu.
plt.title("Najwyzsza i najnizsza temperatura dnia, 2018", fontsize=24)
plt.xlabel('', fontsize=26)
fig.autofmt_xdate()
plt.ylabel("Temperatura (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()