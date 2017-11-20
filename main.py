import sys
import time
import datetime
import pprint
import cryptocompare as cc

def main(argv):
    period = 10

    while True:

        ##this code is executed every period

        print('10 second period started')

        time.sleep(period) ##rest 10 seconds


if __name__ == "__main__":
    main(sys.argv[1:])
