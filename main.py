import sys
import time
import datetime
import pprint ##formatted printing

##get live crypto index prices
import cryptocompare as cc

import forex_python.converter as fiat
##use USD and convert to CAD instead of directly using CAD as the index price, as more volume in USD means its more represenative of the changing market

##import local py files
import settings
import market_data
import analysis

quadriga_summary = market_data.QuadrigaSummary()
order_book = market_data.OrderBook()
price_history = analysis.History()

def main(argv):
    period = 10

    while True:

        print('10 second period started')
        ##this code is executed every period

        quadriga_summary.update()
        order_book.update()

        indexprice = fiat.convert('USD','CAD', cc.get_price(settings.CURRENCY.upper(),curr='USD',full=True)['RAW'][settings.CURRENCY.upper()]['USD']['PRICE'])
        print(indexprice)

        print(order_book.asks[0])

        price_history.appendPrice(indexprice)
        print('MA: ', price_history.getMovingAverage())
        time.sleep(period) ##rest 10 seconds


if __name__ == "__main__":
    main(sys.argv[1:])
