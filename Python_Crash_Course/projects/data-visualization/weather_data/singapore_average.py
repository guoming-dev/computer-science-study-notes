from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('./singapore_changi_international_2024_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and average temperatures.
dates, temps = [], []
for row in reader:
    current_date = datetime.strptime(row[5], '%Y-%m-%d')
    average_temp = int(row[6])
    dates.append(current_date)
    temps.append(average_temp)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, temps, color='red')

# Format plot.
title = "Average Temperature, 2024\nSingapore Changi International, SN"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()