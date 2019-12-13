"""
Name: Group
Group Names: Nicholas Drake, Matthew Rubin, Benjamin Albright
File Name: japi.py
Project: PD 5
Purpose: To build a program that takes JSON format to string to display the current stock symbol and price.
"""
# Import Area
import urllib.request
import json
import sys
# Functions Area
# API: RG03FKYZQIPPCMJM


def main():
    # for some reason appl stock has an error
    stocksymbol = input("Enter a stock symbol(ex: msft, amzn) type \'quit\' to exit: ")
    if stocksymbol == 'quit':
        exit()
    else:
        getstockdata(stocksymbol)


def getstockdata(symbol):

    myapi = 'RG03FKYZQIPPCMJM'
    urlmain = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + symbol + '&apikey=' + myapi
    connection = urllib.request.urlopen(urlmain)

    response = json.load(connection)
    currentprice = float(response['Time Series (Daily)']['2019-12-12']['1. open'])
    print('The current open price for ', symbol, ' is: $', round(currentprice, 3))

    # Sending the print to the Japiout.txt
    f = open('japiout.txt', 'a')
    print('The current open price for ', symbol, ' is: $', round(currentprice, 2), file=f)



main()
