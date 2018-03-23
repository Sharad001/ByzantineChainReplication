class ResultStatement:
	def __init__(self):
		self.operation = None
		self.result = None
	
	def __str__(self):
		return str(self.operation)+";"+self.result.decode('utf-8')

