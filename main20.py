import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import altair as alt

days = 20
tickers = {
    "apple":"AAPL",
    "facebook":"META",
    "google":"GOOGL",
    "microsoft":"MSFT",
    "netflix":"NFLX",
    "amazon":"AMZN",
}

def get_data(days, tickers):
	df=pd.DataFrame()
	for company in tickers.keys():
		tkr = yf.Ticker(tickers[company])
		hist = tkr.history(period=f'{days}d')
		hist.index = hist.index.strftime("%d %B %Y")
		hist = hist[["Close"]]
		hist.columns = [company]
		hist = hist.T
		hist.index.name = "Name"
		df = pd.concat([df,hist]) 
	return df
    
df = get_data(days, tickers)

print(df)

