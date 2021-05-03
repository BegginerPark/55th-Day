import pybithumb
import time

con_key = "346249036fceebe003f790bdd63f6997	"
sec_key = "1166d0aed01d4ba9e822002d85dea922"

bithumb = pybithumb.Bithumb(con_key, sec_key)

for ticker in pybithumb.get_tickers():
    balance = bithumb.get_balance("BTC")
    print(ticker, ":", balance)
    time.sleep(0.1)