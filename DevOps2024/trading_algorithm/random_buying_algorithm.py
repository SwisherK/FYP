# trading_framework/algorithms/random_buying_algorithm.py

import pandas as pd
import numpy as np
from . import TradingAlgorithm

class RandomBuyingAlgorithm(TradingAlgorithm):
    def __init__(self, buy_prob=0.1):
        self.buy_prob = buy_prob

    def generate_signals(self, historical_data):
        signals = pd.DataFrame(index=historical_data.index)
        signals['price'] = historical_data
        signals['signal'] = np.random.choice([0, 1], size=len(historical_data), p=[1-self.buy_prob, self.buy_prob])
        signals['positions'] = signals['signal'].diff().fillna(0)
        return signals
