import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import altair as alt
from altair_saver import save

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

companies = ["apple","facebook"]
data = df.loc[companies]

data.sort_index()

data = data.T.reset_index()

data = pd.melt(data, id_vars=["Date"]).rename(columns={"value": "stock prices"})

ymin, ymax = 100, 200

chart = (
	alt.Chart(data).mark_line(opacity=0.8, clip=True).encode(
	 x="Date:T",
	 y=alt.Y("stock prices:Q", stack=None, scale=alt.Scale(domain=[ymin,ymax])),
	 color="Name:N"
	)
)
save(chart, "chart.html", embed_options={"actions": True})


