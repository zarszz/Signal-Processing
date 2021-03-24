import pandas
import matplotlib.pyplot as plt

from scipy.signal import butter, filtfilt

# reference
# https://www.kite.com/python/answers/how-to-create-a-low-pass-filter-in-python
# https://dsp.stackexchange.com/questions/49460/apply-low-pass-butterworth-filter-in-python

# load data
data = pandas.read_csv('2.csv')['1645']

# amount of data
amount = list(range(0, len(data)))

frequency_sampling = 1000
cutoff_freq = 30
order = 5

normalized_cutoff_freq = cutoff_freq / (frequency_sampling / 2)

b, a = butter(order, normalized_cutoff_freq, 'low')
filtered_signal = filtfilt(b, a, data)

plt.plot(amount, data, 'b-', label='signal', color='red')
plt.plot(amount, filtered_signal, 'g-', linewidth=2, label='filtered signal', color='blue')
plt.legend()
plt.savefig('lpf')
plt.show()
