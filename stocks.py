
class Stock:

    def __init__(self, buy_price, current, amt, dif):
        self.buy_price = buy_price
        self.current = current
        self.amt = amt
        self.dif = dif
        self.diff = 0
        self.total = 0

    def get_buy_price(self):
        return self.buy_price

    def get_current(self):
        return self.current

    def get_amt(self):
        return self.amt

    def calc_diff(self):
        print(self.current)
        print(self.buy_price)
        self.diff = self.current - self.buy_price
        if self.diff < 0:
            print("Loss: %.2f" %(self.diff))
        else:
            print("Gained: %.2f" %(self.diff) + " per share")

    def calc_total(self):
        self.total = self.diff * self.amt
        print("Total: %.2f" %(self.total))

    def get_dif(self):
        return self.dif

def main():
    total = 0
    owned = ["NVDA", "TWLO", "APPN", "PAYC", "SHOP", "NOW"]
    buyprice = [359.94, 183.05, 53.74, 285.04, 745.42, 390]
    shares = [2, 5, 20, 4, 2, 2]

    for j in range(0, len(owned)):
        y = buyprice[j]
        z = float(input("Enter the current price for " + owned[j]))
        amt = shares[j]
        dif = (z - y) * amt
        total += dif
        newstock = Stock(y, z, amt, dif)
        newstock.calc_diff()
        newstock.calc_total()
    print ('Profit: %.2f' % (total))
main()