import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)

    if response.status_code != 200:
        print("\nError fetching exchange rate data.")
        return
    
    data = response.json()
    rates = data["rates"]

    if to_currency.upper() not in rates:
        print("\nInvalid target currency.")
        return
    
    converted = amount * rates[to_currency.upper()]

    print(f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")

# main menu of the program
print("Welcome!")
amount = float(input("\nPlease enter the amount you would like to convert: "))
from_currency = input("\nEnter the currency you have (e.g. USD): ")
to_currency = input("\nEnter the currency you want to convert to (e.g. CAD): ")

convert_currency(amount, from_currency, to_currency)