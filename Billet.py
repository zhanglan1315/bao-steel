# steel.py
class Billet:
	# dataSource
	thick: ''
	width: ''
	discharge: ''
	rm_time_1: ''
	fm_time_1: ''
	steelspec: ''
	staying_time_pre: ''
	staying_time_1: ''
	staying_time_2: ''
	staying_time_soak: ''
	in_fce_time: ''
	upid: ''
	da_1: ''
	wait_t_1: ''

	def __init__ (self, row):
		self.setFromPandasCsvRow(row)
		return

	def setFromPandasCsvRow (self, row):
		self.thick = round(row['tgtplatethickness1'], 4)
		self.width = round(row['tgtwidth'], 3)
		self.discharge = round(row['discharge'], 3)
		self.rm_time_1 = round(row['rm_time'], 3)
		self.fm_time_1 = round(row['fm_time'], 3)
		self.steelspec = row['steelspec']
		self.staying_time_pre = row['staying_time_pre']
		self.staying_time_1 = row['staying_time_1']
		self.staying_time_2 = row['staying_time_2']
		self.staying_time_soak = row['staying_time_soak']
		self.in_fce_time = row['in_fce_time']
		self.upid = row['upid']
		self.da_1 = round(row['cooltime'], 3)
		self.wait_t_1 = round(row['discharge_rm-fm'], 3)
