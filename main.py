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
        print('#####')
        print('#####')
        ##this code is executed every period

        quadriga_summary.update()
        order_book.update()

        indexprice = fiat.convert('USD','CAD', cc.get_price(settings.CURRENCY.upper(),curr='USD',full=True)['RAW'][settings.CURRENCY.upper()]['USD']['PRICE'])
        price_history.appendPrice(indexprice)

        #if(indexprice > price_history.getMovingAverage()):
        #    print('above total MA')
        #    if(indexprice > price_history.getMovingAverageForMinutes(5)):
        #        print('also above 5 min MA')

        print('available price: ', order_book.asks[0][0])
        print('index price: ', indexprice)
        analysis.checkIfGoodDeal(float(order_book.asks[0][0]), indexprice, True)

        print('--')

        print('available price: ', order_book.bids[0][0])
        print('index price: ', indexprice)
        analysis.checkIfGoodDeal(float(order_book.bids[0][0]), indexprice, False)

        time.sleep(period) ##rest 10 seconds

if __name__ == "__main__":
    main(sys.argv[1:])
