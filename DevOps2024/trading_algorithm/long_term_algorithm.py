import pandas as pd
from . import TradingAlgorithm

class LongTermTradingAlgorithm(TradingAlgorithm):
    def generate_signals(self, historical_data):
        signals = pd.DataFrame(index=historical_data.index)
        signals['price'] = historical_data
        signals['signal'] = 1.0  # Always hold the stock
        signals['positions'] = signals['signal'].diff().fillna(0)
        return signals