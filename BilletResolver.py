# BilletResolver.py

from pandas import read_csv
from Billet import Billet
from BilletKind import BilletKind

# 读取数据，顺便排个序
def preloadFromCsv (file):
  dataSource = read_csv(file)
  dataSource.sort_values(by = [
    'steelspec',
    'tgtwidth',
    'tgtplatethickness1',
  ])

  return dataSource

# 遍历 dataFrame
# 首先实例化 billet 对象，再将起分配到指定的 billetKind 中
# 如果分配失败，则以该 billet 为根据创建新的 billetKind
def getBilletsKinds (dataSource):
  kind = BilletKind(Billet(dataSource.loc[0]))
  kinds = []

  for _, billet in dataSource.iterrows():
    billet = Billet(billet)  
    if kind.add(billet) == False:
      kinds.append(kind)
      kind = BilletKind(billet)

  return kinds
