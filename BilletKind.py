# BilletKind.py

# 分类区间参数
WIDTH = 0.005
THICK = 0.0003

# 需要统计端点值的属性
RANGE_ATTRS = [
	'discharge', 'rm_time_1', 'fm_time_1',
	'staying_time_pre', 'staying_time_1',
	'staying_time_2', 'staying_time_soak',
	'in_fce_time', 'da_1', 'wait_t_1'
]

class BilletKind:
	# 分类条件信息
	thick: ''
	width: ''
	steelspec: ''
	isSetted = False

	# 分类数据
	billets = []

	# 统计数据
	ranges = {}

	# 允许初始化时暂时不确定 billet
	# 调用 __setBillet() 时才是真正的初始化
	def __init__ (self, billet = None):
		if billet != None: self.__setBillet(billet)

	# 向分类中添加 billet
	# 如果添加成功，返回 True, False
	# 当 isSetted = false 时，直接添加该 billet
	def add (self, billet):
		if self.isSetted == False:
			self.__setBillet(billet)
			return True
		elif (
			self.__isSpecValid(billet.steelspec) and
			self.__isWidthValid(billet.width) and
			self.__isThickValid(billet.thick)
		):
			self.__handleBilletAppend(billet)
			return True
		else: return False

  # 添加一个 billet 并根据它设置相关的分类条件信息
	def __setBillet (self, billet):
		self.ranges = {}
		self.billets = []
		self.thick = billet.thick
		self.width = billet.width
		self.steelspec = billet.steelspec
		self.billets.append(billet)
		self.isSetted = True
		for attr in RANGE_ATTRS:
			self.ranges[attr] = [None, None]

	# 设置属性
	def __handleBilletAppend (self, billet):
		for attr in RANGE_ATTRS:
			self.__setRange(attr, billet.__dict__[attr])
		self.billets.append(billet)

	# 设置范围
	def __setRange (self, attr, value):
		_range = self.ranges[attr]
		if _range[0] == None:
			_range[0] = _range[1] = value
		if value < _range[0]:
			_range[0] = value
		if value > _range[1]:
			_range[1] = value

	# 分类条件函数
	def __isSpecValid (self, spec):
		return spec == self.steelspec

	def __isWidthValid (self, width):
		return width < (self.width + WIDTH)

	def __isThickValid (self, thick):
		return thick < (self.thick + THICK)
