from base import *
import json

f = open('./config/ma.json', 'r')
config = json.load(f)

api_key = config['api_key']
secret_key = config['secret_key']
symbol = config['symbol']
url = config['url']
kline_size = config['kline_size']

logger = get_logger()

b = Base(api_key, secret_key, url, logger)

# print(b.get_kline(symbol, kline_size = kline_size, kline_num = 5))
eth = b.get_available('eth')
print(eth)
# print(b.spot.sell('eth_usdt', 230, eth, 1))

usdt = b.get_available('usdt')
print(usdt)
print(b.spot.buy('eth_usdt', 211, usdt, 1))

