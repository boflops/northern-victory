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
        fiveminlist = self.recentprices[len(self.recentprices) - (periods) - 1:len(self.recentprices)-1]

        return sum(fiveminlist) / periods ##return MA over this period

def checkIfGoodDeal(availablePrice, indexedPrice, bull):
    if(bull):
        div = indexedPrice / availablePrice
        if(div > settings.TRIGGER_DIFFERENCE):
            print('buy from this sucker')
            return True
        return False

    else:
        div = availablePrice / indexedPrice
        if(div > settings.TRIGGER_DIFFERENCE):
            print('sell to this sucker')
            return True
        return False
