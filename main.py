# main.py
import BilletResolver

def main():
  data = BilletResolver.preloadFromCsv('./dataSource.csv')
  kinds = BilletResolver.getBilletsKinds(data)
  for key, kind in enumerate(filter(
    lambda k: len(k.billets) > 100, kinds)
  ):
    kind.aggregator.compute()
    kind.aggregator.generateChart('./result-charts', key)

main()
