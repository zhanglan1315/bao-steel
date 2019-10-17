# BilletKind.py
from BilletKindAggregator import BilletKindAggregator

# 分类区间参数
WIDTH = 0.005
THICK = 0.0003

# billet 分类
# 它时满足特定条件的 billet 数据
class BilletKind:
	# isSetted 表示 BilletKind 是否已初始化
	# 未初始化时，BilletKind 的分类条件不确定
	# 初始化依赖一个 billet，并从中提取分类条件
	# 初始化后，能够使用 add 方法添加满足条件的数据
	isSetted = False

	# 分类条件
	thick: ''
	width: ''
	steelspec: ''

	# 该分类下的数据
	billets = []

	# 数据统计器
	aggregator = {}

	# 如果创建分类时传入了 billet 数据，那么将执行初始化
	def __init__ (self, billet = None):
		self.aggregator = BilletKindAggregator(self)
		if billet != None: self.__setBillet(billet)

	# 向分组中添加一个 billet
	# 根据分类条件决定是否添加成功
	# 如果添加成功，返回 True, 否则返回 False
	# 当 isSetted 为 false 时，直接用该 billet 初始化分类
	def add (self, billet):
		if self.isSetted == False:
			self.__setBillet(billet)
			return True
		elif (
			self.__isSpecValid(billet.steelspec) and
			self.__isWidthValid(billet.width) and
			self.__isThickValid(billet.thick)
		):
			self.billets.append(billet)
			# 添加后将数据交给 aggregator 处理
			self.aggregator.handleBilletAdded(billet)
			return True
		else: return False

	# 添加 billet，并初始化分类
	def __setBillet (self, billet):
		self.ranges = {}
		self.billets = []
		self.thick = billet.thick
		self.width = billet.width
		self.steelspec = billet.steelspec
		self.billets.append(billet)
		self.isSetted = True

	# 分类条件函数
	def __isSpecValid (self, spec):
		return spec == self.steelspec

	def __isWidthValid (self, width):
		return width < (self.width + WIDTH)

	def __isThickValid (self, thick):
		return thick < (self.thick + THICK)
