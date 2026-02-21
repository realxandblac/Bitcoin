from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/price', methods=['GET'])
def get_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    data = response.json()
    price = data['bpi']['USD']['rate']
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)