# Crypto Arbitrage Monitor

A real-time statistical arbitrage monitoring system built in Python that detects cryptocurrency price differences between exchanges and identifies potential market inefficiencies.

This project **does not execute real trades**. It is a market monitoring and analysis system that uses live exchange data to simulate arbitrage detection.

---

# Overview

Cryptocurrency prices can differ slightly between exchanges due to market inefficiencies, liquidity differences, and timing delays.

This project monitors multiple exchanges simultaneously, compares their order books, calculates potential arbitrage opportunities after simulated trading fees, and detects unusual market behavior using statistical analysis.

---

# Features

## Real-Time Market Monitoring

- Fetches live cryptocurrency order book data
- Connects to multiple exchanges using CCXT
- Tracks:
  - Bid prices (highest buying price)
  - Ask prices (lowest selling price)

---

## Arbitrage Opportunity Detection

The system compares prices between exchanges:

```
Spread = Selling Price - Buying Price
```

It then:

- Calculates potential profit
- Simulates exchange trading fees
- Determines if an opportunity remains profitable after costs
- Logs potential opportunities

---

## Statistical Market Anomaly Detection

The system analyzes historical spread behavior using Z-score analysis.

Z-score measures how far the current spread is from its historical average:

```
Z-score = (Current Spread - Average Spread) / Standard Deviation
```

Events where:

```
|Z-score| > 2
```

are flagged as unusual market movements and logged.

---

## Interactive Dashboard

Built with Streamlit.

The dashboard contains two sections:

### Arbitrage Opportunities

Displays:

- Profit history
- Spread changes
- Trading fees
- Logged opportunities


### Market Anomalies

Displays:

- Z-score movements
- Statistical deviations
- Detected market events

---

# Architecture

```
                         Exchange APIs
                              |
                              v
                            CCXT
                              |
                              v
                    Order Book Processing
                              |
              --------------------------------
              |                              |
              v                              v
       Arbitrage Analysis            Statistical Analysis
              |                              |
              v                              v
        trades.csv                    events.csv
              |                              |
              --------------------------------
                              |
                              v
                    Streamlit Dashboard
                  /                    \
                 v                      v
        Profit Opportunities      Market Anomalies
```

---

# Tech Stack

## Languages

- Python

## Libraries

- CCXT
- Streamlit
- Matplotlib

## Concepts Used

- API integration
- Real-time data processing
- Financial calculations
- Statistical analysis
- Data visualization
- Logging systems

---

# Project Structure

```
crypto-arbitrage-monitor/

├── main.py              # Main monitoring loop
├── dashboard.py         # Streamlit dashboard
├── arbitrage.py         # Arbitrage profit calculations
├── stats.py             # Z-score calculations
├── utils.py             # Exchange utilities
├── logger.py            # Trade logging
├── event_logger.py      # Market event logging
├── graph.py             # Graphing utilities
├── requirements.txt     # Python dependencies
├── README.md            # Documentation
│
└── logs/
    ├── trades.csv       # Arbitrage opportunities
    └── events.csv       # Statistical events
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
```

Move into the project:

```bash
cd crypto-arbitrage-monitor
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# Running the Project

## Start Market Monitor

Run:

```bash
python main.py
```

The program will:

- Connect to exchanges
- Fetch live order books
- Calculate spreads
- Detect opportunities
- Log events

---

## Start Dashboard

Run:

```bash
streamlit run dashboard.py
```

The dashboard will open at:

```
http://localhost:8501
```

---

# Example Output

```
CRYPTO ARBITRAGE MONITOR

COINBASE

Bid: $63,574.28
Ask: $63,574.29


BINANCE

Bid: $63,580.00
Ask: $63,580.10


COINBASE → BINANCE

Spread: $5.71
Fees: $127.14
Profit: -$121.43

Z-score: 2.81

UNUSUAL MARKET EVENT
```

---

# Logging

The system automatically creates:

## trades.csv

Stores potential arbitrage opportunities:

```
Time
Buy Exchange
Sell Exchange
Spread
Fees
Profit
```

---

## events.csv

Stores unusual market movements:

```
Time
Direction
Z-score
Spread %
```

# DISCLAIMER

This project is for educational and research purposes only.

It does not execute real cryptocurrency trades and should not be considered financial advice or a trading system.