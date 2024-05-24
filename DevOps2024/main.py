# trading_framework/main.py

import matplotlib.pyplot as plt
from data.data_retrieval import get_multiple_stocks_data
from trading_algorithm.long_term_algorithm import LongTermTradingAlgorithm
from trading_algorithm.random_buying_algorithm import RandomBuyingAlgorithm
from trading_algorithm.trend_following_algorithm import TrendFollowingAlgorithm
from simulation.simulator import TradingSimulator
from evaluation.performance import evaluate_performance
from data.tickers import tickers

# Rest of the script remains the same...


# Configuration
start_date = '2020-01-01'
end_date = '2021-01-01'
initial_cash = 10000

# Fetch data
historical_data = get_multiple_stocks_data(tickers, start_date, end_date)

# Initialize algorithms
long_term_algorithm = LongTermTradingAlgorithm()
random_buying_algorithm = RandomBuyingAlgorithm(buy_prob=0.05)
trend_following_algorithm = TrendFollowingAlgorithm(short_window=40, long_window=100)

# Initialize simulators
long_term_simulator = TradingSimulator(initial_cash=initial_cash, algorithm=long_term_algorithm)
random_buying_simulator = TradingSimulator(initial_cash=initial_cash, algorithm=random_buying_algorithm)
trend_following_simulator = TradingSimulator(initial_cash=initial_cash, algorithm=trend_following_algorithm)

# Run simulations
long_term_portfolios = long_term_simulator.simulate_multiple(historical_data)
random_buying_portfolios = random_buying_simulator.simulate_multiple(historical_data)
trend_following_portfolios = trend_following_simulator.simulate_multiple(historical_data)

# Evaluate performance for each strategy
def evaluate_strategies(portfolios):
    total_returns = {}
    for ticker, portfolio in portfolios.items():
        total_returns[ticker] = evaluate_performance(portfolio, initial_cash)
    average_return = sum(total_returns.values()) / len(total_returns)
    return average_return

long_term_avg_return = evaluate_strategies(long_term_portfolios)
random_buying_avg_return = evaluate_strategies(random_buying_portfolios)
trend_following_avg_return = evaluate_strategies(trend_following_portfolios)

print(f"Long-term strategy average return: {long_term_avg_return:.2%}")
print(f"Random buying strategy average return: {random_buying_avg_return:.2%}")
print(f"Trend-following strategy average return: {trend_following_avg_return:.2%}")

# Example plotting for one stock (AAPL) using trend-following strategy
ticker_to_plot = 'AAPL'
signals = trend_following_algorithm.generate_signals(historical_data[ticker_to_plot])
plt.figure(figsize=(14, 7))
plt.plot(historical_data[ticker_to_plot].index, historical_data[ticker_to_plot], label='Price')
plt.plot(signals['short_mavg'], label='Short Moving Average')
plt.plot(signals['long_mavg'], label='Long Moving Average')
plt.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], '^', markersize=10, color='g', lw=0, label='Buy Signal')
plt.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 'v', markersize=10, color='r', lw=0, label='Sell Signal')
plt.legend()
plt.show()
