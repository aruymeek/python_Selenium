from model.stock import StockModel

f = open(r'C:\Users\671\Desktop\y\python\chrometest\stock.txt', 'r', encoding="utf-8")

lines = f.readlines()
stock_list = []

for line in lines:
    items = line.split(';')

    nation = items[0].strip()
    index = items[1].strip()
    now = format(float(items[2].strip()), ',')
    diff = float(items[3].strip())
    percent = float(items[4].strip())

    stock = StockModel(nation, index, now, diff, percent)
    stock_list.append(stock)

for s in stock_list:
    data = s.ReadFormat()
    print(data)


