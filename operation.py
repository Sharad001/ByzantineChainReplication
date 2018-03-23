class Operation:
	def __init__(self):
		self.requestId = None
		self.slotNo = None
		self.command = None
		self.key = None
		self.value = None

	def isEqual(self, operation):
		if (self.value == operation.value
			and self.requestId == operation.requestId
			and self.key == operation.key
			and self.command == operation.command
			and self.slotNo == operation.slotNo):
			return True
		else:
		 	return False

	def __str__(self):
		return str(self.requestId)+";"+str(self.slotNo)+";"+self.command+";"+self.key+";"+str(self.value)

	def getWorkload(self, operation_object):
		command = operation_object.command
		key = operation_object.key
		value = operation_object.value
		if value == "":
			actual_workload = command + "("+key+")"
		else:
			actual_workload = command + "("+key+","+value+")"
		return actual_workload.replace(' ','').strip()
