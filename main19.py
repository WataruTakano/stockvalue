import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

print("main")
appl = yf.Ticker("AAPL")
#print(appl.history())
#print(appl.history(period='50d').shape)
#print(appl.history(period='max').shape)

days = 20
hist = appl.history(period=f'{days}d')

#print(hist.columns)
#print(hist.reset_index())

hist_msft = yf.Ticker("MSFT").history(period=f'{days}d')
print(hist_msft)

concat_hist = pd.concat([hist, hist_msft], axis=1)

print(concat_hist)

print(hist.index)

hist.index = hist.index.strftime('%d %B %Y')
print(hist.index)

hist = hist[['Close']]
hist.columns = ['apple']
print(hist)

hist = hist.T
hist.index.name = "Name"
print(hist)