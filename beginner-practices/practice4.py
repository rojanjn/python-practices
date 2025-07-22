# building a dictionary and using methods to alter it
fruit_prices = {
    "apple": 1500,
    "banana": 1000,
    "orange": 1200
}

fruit_prices["banana"] = 1100
fruit_prices.pop("apple")

print(fruit_prices)