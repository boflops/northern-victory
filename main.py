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

        ma5 = price_history.getMovingAverageForMinutes(1)

        ema20 = price_history.getExpMovingAverageForMinutes(1)

        print("MA5: ", ma5)
        print("EMA: ", ema20)
        ##BUY
        if(priceticker > price_history.getMovingAverage()):
            print('avove total MA, price increasing..')
            if(ma5 is None):
                print('no ma5 YET..')
            else:
                #print('ma5: ', ma5)
                if(analysis.checkIfGoodDeal(float(order_book.asks[0][0]), priceticker, True)):
                    print("buy this: ", order_book.asks[0])
                    print('its a good deal as the bitfinex price is: ', priceticker)

        ##SELL
        if(priceticker < price_history.getMovingAverage()):
            print('under total MA, price decreasing..')
            if(ma5 is None):
                print('no MA5 yet..')
            else:
                #print('ma5: ', ma5)
                if(analysis.checkIfGoodDeal(float(order_book.bids[0][0]), priceticker, False)):
                    print("sell this: ", order_book.bids[0])
                    print('its a good deal as the bitfinex price is: ', priceticker)


        time.sleep(period) ##rest 10 seconds (end of loop)


if __name__ == "__main__":
    main(sys.argv[1:])
