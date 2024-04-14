import yfinance

def saveDictionary(d, fn):
  f = open(fn, 'w')
  for k, v in d.items():
      mystr = str(k) + ',' + str(v) + '\n'
      f.write(mystr)
  f.close()
  return

def readToDictionary(fn):
    f = open(fn,'r')
    lines = f.read()
    f.close()
    d = {}
    for line in lines.split('\n'):
        kvlist = line.split(',')
        if len(kvlist[0]) > 0:
            k = kvlist[0]
            v = kvlist[1]
            d[k] = int(v)
    return d

def getPrices(stockList, mydate):
    prices = {}
    for stock in stockList:
        df = yfinance.download(stock, mydate)
        price = df.loc[mydate]['Close']
        prices[stock] = round(price,2)
    return prices