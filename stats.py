import statistics

spread_history_ab = []
spread_history_ba = []

def add_spread_ab(spread):
    spread_history_ab.append(spread)

    if len(spread_history_ab) > 100:
        spread_history_ab.pop(0)

def add_spread_ba(spread):
    spread_history_ba.append(spread)

    if len(spread_history_ba) > 100:
        spread_history_ba.pop(0)

def calculate_z_score(history, current_spread):

    if len(history) < 10:
        return 0

    mean = statistics.mean(history)

    deviation = statistics.stdev(history)

    if deviation == 0:
        return 0

    return (
        (current_spread - mean)
        /
        deviation
    )