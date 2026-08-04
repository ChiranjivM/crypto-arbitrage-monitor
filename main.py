import time
import os

from config import *
from utils import create_exchange, get_orderbook
from arbitrage import calculate_profit
from logger import initialize_log, log_trade
from stats import (spread_history_ab, spread_history_ba, add_spread_ab, add_spread_ba, calculate_z_score)
from event_logger import initialize_event_log, log_event

exchange_a = create_exchange(EXCHANGE_A)
exchange_b = create_exchange(EXCHANGE_B)

#create trades.csv
initialize_log()

#create events.csv
initialize_event_log()

last_event_time_ab = 0
last_event_time_ba = 0

#cooldown for logging unusual market events to avoid spamming the log file
EVENT_COOLDOWN = 60

print("Crypto Arbitrage Monitor")
print("-" * 40)

while True:
    try:
        #clear terminal for better readability
        os.system("cls" if os.name == "nt" else "clear")

        bid_a, ask_a = get_orderbook(
            exchange_a,
            SYMBOL
        )

        bid_b, ask_b = get_orderbook(
            exchange_b,
            SYMBOL
        )

        print("Crypto Arbitrage Monitor")
        print("-" * 40)

        print(EXCHANGE_A.upper())

        print(
            f"Bid: ${bid_a:,.2f}"
        )

        print(
            f"Ask: ${ask_a:,.2f}"
        )

        print()

        print(EXCHANGE_B.upper())

        print(
            f"Bid: ${bid_b:,.2f}"
        )

        print(
            f"Ask: ${ask_b:,.2f}"
        )

        #buy a, sell b
        result_ab = calculate_profit(
            ask_a,
            bid_b
        )

        #buy b, sell a
        result_ba = calculate_profit(
            ask_b,
            bid_a
        )

        spread_ab = result_ab["spread_percentage"]

        spread_ba = result_ba["spread_percentage"]


        add_spread_ab(spread_ab)

        add_spread_ba(spread_ba)


        z_score_ab = calculate_z_score(
            spread_history_ab,
            spread_ab
        )


        z_score_ba = calculate_z_score(
            spread_history_ba,
            spread_ba
        )

        print("\nOpportunities")
        print("-" * 30)

        print(
            f"{EXCHANGE_A} → {EXCHANGE_B}"
        )

        print(
            f"Spread: ${result_ab['spread']:.2f}"
        )

        print(
            f"Spread %: {result_ab['spread_percentage']:.4f}%"
        )

        print(
            f"Z-score: {z_score_ab:.2f}"
        )

        print(
            f"Fees: ${result_ab['fees']:.2f}"
        )

        print(
            f"Profit: ${result_ab['profit']:.2f}"
        )

        print()


        print(
            f"{EXCHANGE_B} → {EXCHANGE_A}"
        )

        print(
            f"Spread: ${result_ba['spread']:.2f}"
        )

        print(
            f"Spread %: {result_ba['spread_percentage']:.4f}%"
        )

        print(
            f"Z-score: {z_score_ba:.2f}"
        )

        print(
            f"Fees: ${result_ba['fees']:.2f}"
        )

        print(
            f"Profit: ${result_ba['profit']:.2f}"
        )

        #detect unusual market events based on previous behavior of the spread
        if abs(z_score_ab) > 2 and time.time() - last_event_time_ab > EVENT_COOLDOWN:

            print("\nUNUSUAL MARKET EVENT")

            log_event(
                f"{EXCHANGE_A} → {EXCHANGE_B}",
                z_score_ab,
                spread_ab
            )

            print(
                f"{EXCHANGE_A} → {EXCHANGE_B} spread deviation"
            )

            last_event_time_ab = time.time()

        #detect unusual market events based on previous behavior of the spread
        if abs(z_score_ba) > 2 and time.time() - last_event_time_ba > EVENT_COOLDOWN:

            print("\nUNUSUAL MARKET EVENT")

            log_event(
                f"{EXCHANGE_B} → {EXCHANGE_A}",
                z_score_ba,
                spread_ba
            )

            print(
                f"{EXCHANGE_B} → {EXCHANGE_A} spread deviation"
            )

            last_event_time_ba = time.time()

        if result_ab["profit"] > 0:
            print(
                "\nARBITRAGE OPPORTUNITY"
            )

            log_trade(
                EXCHANGE_A,
                EXCHANGE_B,
                result_ab["spread"],
                result_ab["fees"],
                result_ab["profit"]
            )


        if result_ba["profit"] > 0:
            print(
                "\nARBITRAGE OPPORTUNITY"
            )

            log_trade(
                EXCHANGE_B,
                EXCHANGE_A,
                result_ba["spread"],
                result_ba["fees"],
                result_ba["profit"]
            )


    except Exception as e:
        print("ERROR:")
        print(e)

    time.sleep(REFRESH_RATE)