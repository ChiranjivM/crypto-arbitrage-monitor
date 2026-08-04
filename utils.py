import ccxt

def create_exchange(exchange_name):
    exchange_class = getattr(ccxt, exchange_name)

    exchange = exchange_class({
        "enableRateLimit": True,
    })

    return exchange

def get_orderbook(exchange, symbol):
    exchange.load_markets()

    orderbook = exchange.fetch_order_book(symbol)

    bid = orderbook["bids"][0][0]
    ask = orderbook["asks"][0][0]

    return bid, ask