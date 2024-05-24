# trading_framework/algorithms/trend_following_algorithm.py

import pandas as pd
import numpy as np
from . import TradingAlgorithm

class TrendFollowingAlgorithm(TradingAlgorithm):
    def __init__(self, short_window=40, long_window=100):
        self.short_window = short_window
        self.long_window = long_window
    
    def generate_signals(self, historical_data):
        signals = pd.DataFrame(index=historical_data.index)
        signals['price'] = historical_data
        signals['short_mavg'] = historical_data.rolling(window=self.short_window, min_periods=1).mean()
        signals['long_mavg'] = historical_data.rolling(window=self.long_window, min_periods=1).mean()
        signals['signal'] = 0.0
        signals['signal'][self.short_window:] = np.where(signals['short_mavg'][self.short_window:] > signals['long_mavg'][self.short_window:], 1.0, 0.0)
        signals['positions'] = signals['signal'].diff()
        return signals
