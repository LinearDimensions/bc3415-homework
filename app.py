from flask import Flask, render_template, jsonify
import random
import yfinance as yf

app = Flask(__name__)
app.run(host='0.0.0.0')

# Sample financial headlines
headlines = [x['title'] for x in yf.Ticker('SPY').news]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/headline', methods=['GET'])
def get_headline():
    # Return a random headline
    return jsonify({"headline": random.choice(headlines)})

@app.route('/week8')
def week8():
    return render_template('week8.html')

@app.route('/week9')
def week9():
    return render_template('week9.html')

if __name__ == '__main__':
    app.run(debug=True)
