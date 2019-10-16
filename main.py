# main.py
import BilletResolver

def main():
  data = BilletResolver.preloadFromCsv('./dataSource.csv')
  kinds = BilletResolver.getBilletsKinds(data)
  for kind in kinds:
    if (len(kind.billets) > 50):
      print(len(kind.billets))

main()
