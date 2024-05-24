import yfinance as yf


def get_historical_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data['Close']

def get_multiple_stocks_data(tickers, start_date, end_date):
    data = {}
    for ticker in tickers:
        data[ticker] = get_historical_data(ticker, start_date, end_date)
    return data