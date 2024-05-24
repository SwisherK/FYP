# trading_framework/evaluation/performance.py

def evaluate_performance(portfolio, initial_cash):
    total_returns = (portfolio['total'] - initial_cash) / initial_cash
    print(f"Total returns: {total_returns:.2%}")
    return total_returns
