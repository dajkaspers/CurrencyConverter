# Creator: Daj Kaspers
# CurrrencyConverter
# Creation Date: 31/5/2021 

# Import requests to get http request working on script
import requests

# Make class function that converts the currency where USD is the base currency
class CurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        # first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD' :
            amount = amount / self.currencies[from_currency]

        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount

# Function that will ask for input of amount and currency's
def function():
    # Define variables
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = CurrencyConverter(url)
    x = input("\nFrom currency : ")
    y = input("To currency : ")
    z = int(input("Amount : "))
    print("\nAmount of", y, ":", converter.convert(x, y, z))
    
    # Give oppertunity to redo function
    print("\nY will end script, N will resume script")
    okay = input("Type Y/N: ")
    if okay == "Y":
        print("\nStopped")
    elif okay == 'N':
        function()

# Call function
function()
