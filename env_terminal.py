def analyze_data(data):
    growth = data[-1]['value'] - data[0]['value']
    return {
        "growth": growth,
        "percent": (growth / data[0]['value']) * 100
    }
