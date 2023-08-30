import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates 

def converter(data):
    data = str(data)
    return float(data.replace(',', ''))

converters = {
    'Volume': converter,
    'Open': converter,
    'Close': converter,
    'Low': converter,
    'High': converter,
    'Change': converter,
}


stockData = pd.read_csv('stocks.csv', converters=converters, parse_dates=['Date'])
stockData.set_index('Date', inplace=True)
sns.set_style('darkgrid')
description = stockData.describe()
print(description)
date_range = stockData.loc['2013-01-01':'2022-12-31']

# Create a line chart showing the trend of 'Close' prices over time.

# plt.plot(stockData.index, stockData['Close'], 'o--r')
# plt.title("Graph of Close Points")
# plt.xlabel("Date")
# plt.ylabel("Closeing Points")
# plt.show()

# Uniques Values of Volume

uniqueVolume = stockData['Volume']
print()
print()
print("Total Number of Unique Enteries are  ", len(uniqueVolume))

# Highest opening Date 

dateOfHighestOpeing = stockData['Open'].idxmax()

HighestOpeningRow = stockData.loc[dateOfHighestOpeing]

print("Date of the Highest Opening in Stock Market", dateOfHighestOpeing)
print("Opening of the Highest Opening in Stock Market", HighestOpeningRow.Open)
print("Closing of the Highest Opening in Stock Market", HighestOpeningRow.Close)
print("Highest of the Highest Opening in Stock Market", HighestOpeningRow.High)
print("Low of the Highest Opening in Stock Market", HighestOpeningRow.Low)

# Anther way is to sort the data

# another way 

HighestOpeningRow = stockData.nlargest(1, 'Open')
print()
print(type(HighestOpeningRow))
print()

print("The Date of the Higest Opening is ", HighestOpeningRow.index[0])
print("Opening of the Highest Opening in Stock Market", HighestOpeningRow['Open'].values[0])
print("Closing of the Highest Opening in Stock Market", HighestOpeningRow['Close'].values[0])
print("Highest of the Highest Opening in Stock Market", HighestOpeningRow['High'].values[0])
print("Low of the Highest Opening in Stock Market", HighestOpeningRow['Low'].values[0])


# Are there any noticeable trends or patterns in the 'Change' column over time?

# plt.figure(figsize=(10, 6)) 
# n, bins, _ = plt.hist(stockData.index, bins=20, weights=stockData['Change'])
# plt.xlabel('Date')
# plt.ylabel('Frequency')
# plt.title('Histogram of Change')
# plt.plot(bins[:-1], n, marker='o', linestyle='-', color='r', label='Trend')
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format the dates
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

stockData['Volume2'] = stockData['Volume'].shift(1)

stockData['VolumeChange'] = (stockData['Volume'] - stockData['Volume2'])

# plt.figure(figsize=(10, 6)) 
# n, bins , _ = plt.hist(stockData.index, bins=20, weights=stockData['VolumeChange'])

# plt.title('Histogram of Volume Change')
# plt.plot(bins[:-1], n, 'o--r', label="Trends")
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format the dates
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()


# Calculate the percentage change between the 'High' and 'Low' prices for each day. Are there any extreme fluctuations?


stockData['Fluctuations'] = ((stockData['High'] - stockData['Low']) / stockData['Low']) * 100

threshold = 6

dateForExtremeFluctuations = stockData[stockData['Fluctuations'] >= threshold].index
for i in dateForExtremeFluctuations : 
    print(i)




# plt.plot(stockData.index, stockData['Fluctuations'], color='red', alpha= 0.6)
# plt.xlabel('Date')
# plt.ylabel('Fluctuations')
# plt.title('Fluctuations Over Time')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# Create a histogram to visualize the distribution of daily trading volumes.


# plt.plot(date_range.index, date_range['Open'], label='Open')
# plt.plot(date_range.index, date_range['Close'], label='Close', alpha=0.6)
# plt.xlabel('Date')
# plt.ylabel('Value')
# plt.title('Open and Close Prices Over Time (2013-2022)')
# plt.legend()
# plt.xticks(rotation=45)
# plt.tight_layout(pad=2)


# plt.hist([date_range['Open'], date_range['Close']],  label=['Open', 'Close'])
# plt.xlabel('Price')
# plt.ylabel('Frequency')
# plt.title('Histogram of Open and Close Prices')
# plt.legend()
# plt.show()



# print(stockData)

# Calculate the correlation between 'High' and 'Low' prices. What does this imply?
# plt.figure(figsize=(16, 8))

# plt.hist([stockData['High'], stockData['Low']], label=['High', 'Close'])
# plt.legend()  
# plt.xlabel('Date')
# plt.ylabel('Price')  
# plt.title('Stock High and Low Prices Over Time')  

# plt.show()

# Calculate the moving average of the 7-Days

plt.figure(figsize=(10,8))

stockData['7-Day-Moving-Average'] = stockData['Close'].rolling(window=7).mean()

plt.plot(stockData.index, stockData['7-Day-Moving-Average'] )
plt.xlabel("Date")
plt.ylabel("7-Day-Moving-Average")
plt.title("7 Day Moving Average")
plt.show()