import streamlit as st
import csv
import time
import os
import matplotlib.pyplot as plt

TRADES_FILE = "logs/trades.csv"
EVENTS_FILE = "logs/events.csv"

st.set_page_config(
    page_title="Crypto Arbitrage Monitor",
    layout="wide"
)

st.title("Crypto Arbitrage Monitor")

def read_csv_file(filename):
    data = []

    if os.path.exists(filename):

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

    return data

tab1, tab2 = st.tabs(
    [
        "Arbitrage Opportunities",
        "Market Anomalies"
    ]
)

#ARBITRAGE OPPORTUNITIES TAB
with tab1:
    st.header(
        "Profitable Arbitrage Trades"
    )

    trades = read_csv_file(
        TRADES_FILE
    )

    if len(trades) == 0:
        st.info(
            "Waiting for arbitrage opportunities..."
        )

    else:
        profits = []

        for trade in trades:
            profits.append(
                float(trade["Profit"])
            )

        st.subheader(
            "Profit History"
        )

        fig, ax = plt.subplots()

        ax.plot(
            profits,
            marker="o"
        )

        ax.set_xlabel(
            "Trade Number"
        )

        ax.set_ylabel(
            "Profit ($)"
        )

        ax.grid(True)

        st.pyplot(fig)

        st.subheader(
            "Trade Log"
        )

        st.table(
            trades[::-1]
        )

#ANOMALIES TAB
with tab2:
    st.header(
        "Statistical Market Events"
    )

    events = read_csv_file(
        EVENTS_FILE
    )

    if len(events) == 0:
        st.info(
            "No unusual market events detected."
        )

    else:
        z_scores = []

        for event in events:

            z_scores.append(
                float(event["Z-score"])
            )

        st.subheader(
            "Z-score History"
        )

        fig, ax = plt.subplots()

        ax.plot(
            z_scores,
            marker="o"
        )

        ax.axhline(
            2,
            color="red",
            linestyle="--",
            label="Upper threshold"
        )

        ax.axhline(
            -2,
            color="red",
            linestyle="--",
            label="Lower threshold"
        )

        ax.set_xlabel(
            "Event Number"
        )

        ax.set_ylabel(
            "Z-score"
        )

        ax.legend()

        ax.grid(True)

        st.pyplot(fig)

        st.subheader(
            "Event Log"
        )


        st.table(
            events[::-1]
        )

time.sleep(2)

st.rerun()