import requests
import json
from datetime import datetime

class BitcoinTracker:
    def __init__(self):
        self.price_history = []

    def fetch_current_price(self):
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
        data = response.json()
        current_price = data['bpi']['USD']['rate_float']
        self.price_history.append((datetime.now(), current_price))
        return current_price

    def manage_price_history(self, days=30):
        cutoff_date = datetime.now() - timedelta(days=days)
        self.price_history = [entry for entry in self.price_history if entry[0] > cutoff_date]

    def calculate_price_change(self):
        if len(self.price_history) < 2:
            return None
        initial_price = self.price_history[0][1]
        latest_price = self.price_history[-1][1]
        change = ((latest_price - initial_price) / initial_price) * 100
        return change

    def save_data(self, filename='price_history.json'):
        with open(filename, 'w') as f:
            json.dump(self.price_history, f)

    def load_data(self, filename='price_history.json'):
        with open(filename, 'r') as f:
            self.price_history = json.load(f)

# Example usage:
if __name__ == '__main__':
    tracker = BitcoinTracker()
    current_price = tracker.fetch_current_price()
    print(f'Current Bitcoin Price: ${current_price}')