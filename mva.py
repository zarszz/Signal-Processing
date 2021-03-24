import pandas as pd
import matplotlib.pyplot as plt
import random

# reference
# https://towardsdatascience.com/implementing-moving-averages-in-python-1ad28e636f9d

# select D column
data = pd.read_csv('2.csv')['1645']

if str(input("Apakah anda ingin membatasi jumlah data(yes/no) -> ")) == "yes":
    limit = int(input("Masukkan jumlah batasan data (integer, 1 s/d 150.000) -> "))
    data = data[:limit]

# amount of data
amount = list(range(0, len(data)))

# 1st window size experiment is 51
first_window_size = 51

# 2nd window size experiment is get random value from
# first_window_size/2 <= data <= first_window_size
two_window_size = random.randint(int(first_window_size / 2), first_window_size)

# 3th window size experiment is select 10 * first_window_size
three_window_size = first_window_size * 10

# calculate MVA with Pandas rolling function
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html
filtered_data = data.rolling(window=first_window_size).mean()
two_filtered_data = data.rolling(window=two_window_size).mean()
three_filtered_data = data.rolling(window=three_window_size).mean()

# plotting default data
plt.plot(amount, data, label='Normal data', color='blue')

# plotting data with 1st window size (with average data)
plt.plot(amount, filtered_data, label=f'window = {first_window_size}', color='red')

# plotting data with get random value from first_window_size/2 < data < first_window_size
plt.plot(amount, two_filtered_data, label=f'window = {two_window_size}', color='orange')

# plotting data with get random value from first_window_size/2 < data < first_window_size
plt.plot(amount, three_filtered_data, label=f'window = {three_window_size}', color='green')

plt.legend(loc='upper right')

# save a figure and plot data
plt.savefig('mva')
plt.show(block=True)
