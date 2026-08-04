import csv
import time
import matplotlib.pyplot as plt

from config import LOG_FILE

profits = []
times = []

plt.ion()

fig, ax = plt.subplots()

def read_logs():
    profits.clear()
    times.clear()

    try:
        with open(LOG_FILE, "r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                times.append(
                    row["Time"]
                )

                profits.append(
                    float(row["Profit"])
                )

    except FileNotFoundError:
        pass

while True:
    read_logs()

    ax.clear()

    ax.plot(
        profits,
        marker="o"
    )

    ax.set_title(
        "Crypto Arbitrage Profit History"
    )

    ax.set_xlabel(
        "Opportunity"
    )

    ax.set_ylabel(
        "Profit ($)"
    )

    ax.grid(True)

    plt.pause(1)