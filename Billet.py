# steel.py

class Billet:
	# basic data
	upid: ''
	thick: ''
	width: ''
	steelSpec: ''

	# process data
	discharge: ''
	rmTime: ''
	fmTime: ''
	preStayingTime: ''
	firstStayingTime: ''
	secondStayingTime: ''
	soakStayingTime: ''
	inFceTime: ''
	coolTime: ''
	waitTime: ''

	def __init__ (self, row):
		self.setFromPandasCsvRow(row)

	def setFromPandasCsvRow (self, row):
		self.upid = row['upid']
		self.thick = round(row['tgtplatethickness1'], 4)
		self.width = round(row['tgtwidth'], 3)
		self.steelspec = row['steelspec']

		self.discharge = round(row['discharge'], 3)
		self.rmTime = round(row['rm_time'], 3)
		self.fmTime = round(row['fm_time'], 3)
		self.preStayingTime = row['staying_time_pre']
		self.firstStayingTime = row['staying_time_1']
		self.secondStayingTime = row['staying_time_2']
		self.soakStayingTime = row['staying_time_soak']
		self.inFceTime = row['in_fce_time']
		self.coolTime = round(row['cooltime'], 3)
		self.waitTime = round(row['discharge_rm-fm'], 3)
