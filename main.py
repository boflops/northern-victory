import sys
import time
import datetime
import pprint ##formatted printing

##bitfinex is market driver in USD, use this as price reference
import bitfinex
bf_client = bitfinex.Client()


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
        ##this code is executed every period

        ##update quariga trading summary and the quadriga order book
        quadriga_summary.update()
        order_book.update()

        ##update price from bitfinex, convert to CAD and append to the price history list
        priceticker = fiat.convert('USD','CAD', bf_client.ticker(settings.CURRENCY + 'usd')['mid'])
        price_history.appendPrice(priceticker)

        print('-----')

        ##buying oppertunity section
        print('buying oppertunity?')
        if(priceticker > price_history.getMovingAverage()):
            print('under total MA, price increasing..')
            if(type(price_history.getMovingAverageForMinutes(5)) is None):
                print('we have ma5..')
            else:
                if(analysis.checkIfGoodDeal(float(order_book.asks[0][0]), priceticker, True)):
                    print("we are gonna buy this one: ", order_book.asks[0][0])
                    print('its a good deal as the bitfinex price is: ', priceticker)

        print('-----')

        ##buying oppertunity section
        print('selling oppertunity?')

        if(priceticker < price_history.getMovingAverage()):
            print('under total MA, price decreasing..')
            if(type(price_history.getMovingAverageForMinutes(5)) is None):
                print('no ma5 yet')
            else:
                print('we have ma5..')
                if(analysis.checkIfGoodDeal(float(order_book.bids[0][0]), priceticker, False)):
                    print("we are gonna buy this one: ", order_book.bids[0][0])
                    print('its a good deal as the bitfinex price is: ', priceticker)

        time.sleep(period) ##rest 10 seconds

if __name__ == "__main__":
    main(sys.argv[1:])
