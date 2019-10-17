# BilletKindAggregate.py

import scipy
import scipy.stats
import matplotlib.pyplot as plt
from BilletKindHistogram import BilletKindHistogram

# 需要统计的列以及对应的含义
HISTOGRAM_ATTRS = [
  ('discharge', '抽钢时间'),
  ('rmTime', '粗轧时间'),
  ('fmTime', '精轧时间'),
  ('preStayingTime', '预热时间'),
  ('firstStayingTime', '加热段1时间'),
  ('secondStayingTime', '加热段2时间'),
  ('soakStayingTime', '在炉总时间'),
  ('inFceTime', '均热段时间'),
  ('coolTime', 'DQ/ACC时间频数'),
  ('waitTime', '待钢时间'),
]

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 让画出来的图显示中文

class BilletKindAggregator:
  # 列统计器
  histograms = {}

  def __init__ (self, kind):
    self.histograms = {}
    for (attr, text) in HISTOGRAM_ATTRS:
      histogram = BilletKindHistogram(text)
      self.histograms[attr] = histogram

  # 分类中添加数据后，
  def handleBilletAdded (self, billet):
    for (attr, _) in HISTOGRAM_ATTRS:
      self.histograms[attr].addValue(billet.__dict__[attr])

  # 计算统计数据
  def compute (self):
    for (attr, _) in HISTOGRAM_ATTRS:
      histogram = self.histograms[attr]
      histogram.compute()
      self.__printHistogramResult(histogram)
  # 输出图片
  def generateChart (self, path, filename):
    chart = plt.figure(figsize = (20, 20))
    xAxis = [
      chart.add_subplot(521),
      chart.add_subplot(522),
      chart.add_subplot(523),
      chart.add_subplot(528),
      chart.add_subplot(525),
      chart.add_subplot(526),
      chart.add_subplot(527),
      chart.add_subplot(528),
      chart.add_subplot(5, 2, 9),
      chart.add_subplot(5, 2, 10)
    ]
    yAxis = []
    for key, axis in enumerate(xAxis):
      attr = HISTOGRAM_ATTRS[key][0]
      h = self.histograms[attr]
      y = scipy.stats.norm.pdf(h.bins, h.mu, h.sigma)
      yAxis.append(y)
      axis.plot(h.bins, y, label='拟合的正态分布曲线')
      axis.hist(h.values, h.bins, color='g', label='频率分布直方图')
      axis.set_xlabel(h.text + '(t)/s')
      axis.set_title(h.text + '频率分布直方图及拟合正态分布曲线')
      axis.legend()
    chart.tight_layout()
    chart.savefig('./' + path + '/%d.png' % (filename + 1))

  # 输出列统计器的结果
  def __printHistogramResult (self, h):
    for (last, next) in h.limitRanges:
      print (
        '该组 ', h.text, ' 过程中分布频数最高的区间为: ',
        last, '~', next, ', 为 ', h.maxCount, '中点值为: ', (last + next) / 2
      )
    if h.b == 0: return
    print('************************************************')
    print('用方法1给出的该组DQ/ACC时间推荐值为：', round(h.a / h.b, 3))
    print('用方法2给出的该组DQ/ACC时间推荐值为：', round(h.mu, 3))
