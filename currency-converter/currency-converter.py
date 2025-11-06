import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching exchange rate data.")
        return
    
    data = response.json()
    rates = data["rates"]

    if to_currency.upper() not in rates:
        print("Invalid target currency.")
        return
    