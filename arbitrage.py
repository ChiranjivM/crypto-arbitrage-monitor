from config import TRADING_FEE, SIMULATED_TRADE_AMOUNT

def calculate_profit(buy_price, sell_price):
    if buy_price <= 0:
        return {
            "spread": 0,
            "spread_percentage": 0,
            "fees": 0,
            "profit": 0
        }

    spread = sell_price - buy_price

    spread_percentage = (
        (spread / buy_price) * 100
    )

    gross_profit = (
        SIMULATED_TRADE_AMOUNT *
        (spread / buy_price)
    )

    fees = (
        SIMULATED_TRADE_AMOUNT *
        TRADING_FEE *
        2
    )

    profit = gross_profit - fees

    return {
        "spread": spread,
        "spread_percentage": spread_percentage,
        "fees": fees,
        "profit": profit
    }