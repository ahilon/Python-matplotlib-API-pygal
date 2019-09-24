import csv
from matplotlib import pyplot as plt
from datetime import datetime


class Create_comparison_chart():

    def __init__(self, filename, title):
        self.filename = filename
        self.title = title


    def import_data_from_file(self):
        with open(self.filename) as file:
            reader = csv.reader(file)
            header_row = next(reader)

            for index, column_header in enumerate(header_row):
                print(index, column_header)

            dates, highs, lows = [], [], []
            for row in reader:
                try:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    low = int(row[6])
                    high = int(row[5])


                except ValueError:
                    print(current_date, 'Brak danych.')

                else:
                    dates.append(current_date)
                    lows.append(low)
                    highs.append(high)
            print(highs)

            # Dane wykresu
            fig = plt.figure(dpi=128, figsize=(10, 6))
            plt.plot(dates, highs, c='red', alpha=0.5)
            plt.plot(dates, lows, c='blue', alpha=0.5)
            plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

            # Formatowanie wykresu.
            plt.title(self.title, fontsize=24)
            plt.xlabel('', fontsize=26)
            fig.autofmt_xdate()
            plt.ylabel("Temperatura (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)

            plt.show()



filename_1 = 'death_valley_2018_simple.csv'
title = "Najwyzsza i najnizsza temperatura dnia - 2018\nDolina Śmierci"
filename_2 = 'sitka_weather_2018_simple.csv'

file_1 = Create_comparison_chart(filename_1, title)
file_2 = Create_comparison_chart(filename_2, title)

print(file_1.import_data_from_file())
print(file_2.import_data_from_file())