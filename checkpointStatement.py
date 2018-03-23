class CheckpointStatement:
	def __init__(self):
		self.checkpoint_slot = None
		self.running_state = None	 
	
	def __str__(self):
		return str(self.checkpoint_slot) + ";" + self.running_state.decode('UTF-8')
