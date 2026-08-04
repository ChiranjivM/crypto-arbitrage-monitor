import csv
import os
from datetime import datetime

EVENT_FILE = "logs/events.csv"

def initialize_event_log():
    os.makedirs("logs", exist_ok=True)

    if not os.path.exists(EVENT_FILE):

        with open(EVENT_FILE, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Time",
                "Direction",
                "Z-score",
                "Spread %"
            ])

def log_event(direction, z_score, spread):
    with open(EVENT_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            datetime.now(),
            direction,
            round(z_score, 2),
            round(spread, 4)
        ])