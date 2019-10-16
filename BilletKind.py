# BilletKind.py

# 分类区间参数
WIDTH = 0.005
THICK = 0.0003

class BilletKind:
	# 分类条件信息
	thick: ''
	width: ''
	steelspec: ''
	isSetted = False

	# 分类数据
	billets = []

	# 统计结果
	

	# 初始化时未必能够当即确定 billet
	# 因此 billet 参数可能为 None
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
			self.billets.append(billet)
			return True
		else: return False

  # 添加一个 billet 并根据它设置相关的分类条件信息
	def __setBillet (self, billet):
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
