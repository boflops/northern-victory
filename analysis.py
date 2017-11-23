import settings

class History:
    def __init__(self):
        self.recentprices = []

    def appendPrice(self, price):
        self.recentprices.append(price)

    def getMovingAverage(self):
        return sum(self.recentprices) / len(self.recentprices)

    def getMovingAverageForMinutes(self, minutes):

        ##convert minutes into 10 second periods
        periods = minutes * 6
        if(len(self.recentprices) < int(periods)): ##havent been running long enough to get this data
            print("program hasnt been running long enough to get this MA")
            return None
        ##slice list to include only the prices from end of the list for the specified no of minutes
        sublist = self.recentprices[len(self.recentprices) - (periods):len(self.recentprices)]
        return sum(sublist) / periods ##return MA over this period

    def getExpMovingAverageForMinutes(self, minutes):

        ##convert minutes into 10 second periods
        periods = minutes * 6
        if(len(self.recentprices) < int(periods)): ##havent been running long enough to get this data
            print("program hasnt been running long enough to get this EMA")
            return None

        ##slice list to include only the prices from end of the list for the specified no of minutes
        sublist = self.recentprices[len(self.recentprices) - (periods):len(self.recentprices)]

        ##expMA formula:
        ema = 0
        top = 0
        bot = 0
        for i in range (len(sublist)):
            top += sublist[i] * (1 - a(i))**(i - 1)
            bot += (1- a(i))**(i - 1)
        return top / bot ##return EMA over this period

def a(n):
    return (2/(n+1))

def checkIfGoodDeal(availablePrice, indexedPrice, bull):
    if(bull):
        div = indexedPrice / availablePrice
        if(div > settings.TRIGGER_DIFFERENCE):
            return True
        return False

    else:
        div = availablePrice / indexedPrice
        if(div > settings.TRIGGER_DIFFERENCE):
            return True
        return False
