import time
from bs4 import BeautifulSoup
from selenium import webdriver

cost = 6120.93
ticker_dict = {"TWLO": 5, "PAYC": 4, "APPN": 20, "SHOP": 2, "NVDA": 2, "NOW": 2}

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options = options)

total_amt = 0

for ticker in ticker_dict:
    ticker_str = f"https://finance.yahoo.com/quote/{ticker}/history?p={ticker}"
    print("")
    driver.get(ticker_str)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source,"lxml")
    time.sleep(1.2)
    item = soup.find(id="quote-market-notice").find_parent().find("span").text
    stock_amt = float(item.replace(',',''))*ticker_dict[ticker]
    total_amt = total_amt + stock_amt
    print(ticker + ":" + item + ":" + str(stock_amt))

driver.quit()

profit = total_amt - cost
print("")
print(f"Profit = ${profit:.2f}")
total = cost + profit
print(f"Total = ${total:.2f}")
print("")