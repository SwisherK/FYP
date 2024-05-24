# trading_framework/simulation/simulator.py

class TradingSimulator:
    def __init__(self, initial_cash, algorithm):
        self.initial_cash = initial_cash
        self.algorithm = algorithm

    def simulate(self, historical_data):
        portfolio = {'cash': self.initial_cash, 'holdings': 0, 'total': self.initial_cash}
        signals = self.algorithm.generate_signals(historical_data)
        positions = signals['positions']
        
        for date, position in positions.iteritems():
            price = historical_data[date]
            if position == 1.0:  # Buy
                portfolio['holdings'] += portfolio['cash'] / price
                portfolio['cash'] = 0
            elif position == -1.0:  # Sell
                portfolio['cash'] += portfolio['holdings'] * price
                portfolio['holdings'] = 0
            portfolio['total'] = portfolio['cash'] + portfolio['holdings'] * price
        
        return portfolio

    def simulate_multiple(self, historical_data):
        results = {}
        for ticker, data in historical_data.items():
            results[ticker] = self.simulate(data)
        return results
