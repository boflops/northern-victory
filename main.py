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
print(quadriga_summary.timestamp)

def main(argv):
    period = 10

    while True:

        print('10 second period started')
        ##this code is executed every period

        quadriga_summary.update()
        print(quadriga_summary.timestamp)

        time.sleep(period) ##rest 10 seconds


if __name__ == "__main__":
    main(sys.argv[1:])
