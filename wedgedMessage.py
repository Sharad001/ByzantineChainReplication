class WedgedMessage:
	def __init__(self):
		self.history = None
		self.checkpoint_history = None

	def __str__(self):
		return str(self.history) + ';' + str(self.checkpoint_history)
