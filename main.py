import requests
import time
import json
from datetime import datetime

while True:

    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

    response = requests.get(url)

    data = response.json()

    price = data["price"]

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    price_data = {
        "time": current_time,
        "price": price
    }

    print(price_data)

    with open("prices.json", "a") as file:
        json.dump(price_data, file)
        file.write("\n")

    time.sleep(5)
