# BilletKindHistogram.py

import numpy as np
import scipy

# 分类中某一列的数据统计
class BilletKindHistogram:
  text: ''
  # 列数据
  values: []
  # 端点值
  range: []

  a: 0
  b: 0
  mu: 0
  step: 0
  sigma: 0
  binEdge: 0
  maxCount: 0

  bins: []
  counts = []
  limitRanges = []

  def __init__ (self, text):
    self.a = self.b = 0
    self.text = text
    self.range = [None, None]
    self.values = []
    self.bins = []
    self.counts = []
    self.limitRanges = []

  # 添加数据
  # 顺便动态计算端点值
  def addValue (self, value):
    self.values.append(value)
    range = [min, max] = self.range
    if min == None:
      range[0] = range[1] = value
    elif value < min:
      range[0] = value
    elif value > max:
      range[1] = value

  # 计算所有需要的数据
  def compute (self):
    values =  self.values
    [_min, _max] = self.range

    # step
    self.step = (_max - _min) / 100

    # step
    if (self.step == 0): self.bins = np.arange(0, 100, 100)
    else: self.bins = np.arange(_min, _max, self.step)

    # mu, sigma, count, binEdge
    self.mu = np.mean(self.values)
    self.sigma = np.std(self.values)
    self.counts, self.binEdge = np.histogram(values, self.bins)
    self.binEdge = [ round(x) for x in self.binEdge ]

    # maxes, limit_last, limit_
    if (len(self.counts) == 0): return

    self.maxCount = max(self.counts)
    for key, count in enumerate(self.counts):
      if (count != self.maxCount): continue
      last = self.binEdge[key]
      next = self.binEdge[key + 1]
      # limitRange, a, b
      self.limitRanges.append((last, next))
      self.a += (last + next) / 2
      self.b += 1
