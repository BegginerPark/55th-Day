import pybithumb
import time

con_key = "346249036fceebe003f790bdd63f6997	"
sec_key = "1166d0aed01d4ba9e822002d85dea922"

bithumb = pybithumb.Bithumb(con_key, sec_key)

# for ticker in pybithumb.get_tickers():
#     balance = bithumb.get_balance("BTC")
#     print(ticker, ":", balance)
#     time.sleep(0.1)

# order = bithumb.buy_limit_order("BTC", 3900000, 0.001)
# print(order)

krw = bithumb.get_balance("BTC")
orderbook = pybithumb.get_orderbook("BTC")

asks = orderbook['asks']
sell_price = asks[0]['price']
unit = krw/sell_price
print(unit)