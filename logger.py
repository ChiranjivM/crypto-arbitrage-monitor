import csv
import os
from datetime import datetime

from config import LOG_FILE


def initialize_log():

    os.makedirs("logs", exist_ok=True)

    if not os.path.exists(LOG_FILE):

        with open(LOG_FILE, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Time",
                "Buy Exchange",
                "Sell Exchange",
                "Spread",
                "Fees",
                "Profit"
            ])



def log_trade(
        buy_exchange,
        sell_exchange,
        spread,
        fees,
        profit
):

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            buy_exchange,
            sell_exchange,
            round(spread, 2),
            round(fees, 2),
            round(profit, 2)
        ])