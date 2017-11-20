from quadriga import QuadrigaClient
import numpy
import settings

client = QuadrigaClient(
    api_key=settings.API_KEY,
    api_secret=settings.API_SECRET,
    client_id=settings.CLIENT_ID,
    default_book=settings.CURRENCY + '_cad'
)

class QuadrigaSummary:
    def __init__(self):
        summary = client.get_summary()
        self.high = summary['high']
        self.last = summary['last']
        self.timestamp = summary['timestamp']
        self.volume = summary['volume']
        self.vwap = summary['vwap']
        self.low = summary['low']
        self.ask = summary['ask']
        self.bid = summary['bid']

    def update(self):
        summary = client.get_summary()
        self.high = summary['high']
        self.last = summary['last']
        self.timestamp = summary['timestamp']
        self.volume = summary['volume']
        self.vwap = summary['vwap']
        self.low = summary['low']
        self.ask = summary['ask']
        self.bid = summary['bid']

class OrderBook:
    def __init__(self):
        publicorders = client.get_public_orders()
        self.asks = publicorders['asks']
        self.bids = publicorders['bids']
        self.timestamp = publicorders['timestamp']

    def update(self):
        publicorders = client.get_public_orders()
        self.asks = publicorders['asks']
        self.bids = publicorders['bids']
        self.timestamp = publicorders['timestamp']
