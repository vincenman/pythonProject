

import pandas as pd
import datetime
import pandas_datareader.data as pdr
from pandas import Series


aapl = pdr.get_data_yahoo('AAPL', 
                          start=datetime.datetime(2020, 1, 1), 
                          end=datetime.datetime(2020, 7, 29))


adj_close_px = aapl['Adj Close']




# Import matplotlib 
import matplotlib.pyplot as plt

# Short moving window rolling mean
aapl['42'] = adj_close_px.rolling(window=40).mean()

# Long moving window rolling mean
aapl['252'] = adj_close_px.rolling(window=252).mean()

# Plot the adjusted closing price, the short and long windows of rolling means
aapl[['Adj Close', '42', '252']].plot()

# Show plot
plt.show()
