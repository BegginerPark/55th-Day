import pybithumb
import time

con_key = "346249036fceebe003f790bdd63f6997	"
sec_key = "1166d0aed01d4ba9e822002d85dea922"

bithumb = pybithumb.Bithumb(con_key, sec_key)

order = bithumb.sell_limit_order("BTC", 400000000, 1)
print(order)