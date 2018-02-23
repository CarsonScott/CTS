class Variable:

	def __init__(self):
		self.value = None
		self.weights = list()
		self.threshold = int()
		self.constraints = list()

	def get(self):
		return self.value
	
	def set(self, value):
		self.value = value	

	def set_threshold(self, threshold):
		self.threshold = threshold
	
	def add_constraint(self, constraint, weight=1):
		self.constraints.append(constraint)
		self.weights.append(weight)

	def create(self, constraints, weights, threshold):
		self.constraints = constraints
		self.weights = weights

	def compute(self):
		total = 0
		for i in range(len(self.constraints)):
			constraint = self.constraints[i]
			output = constraint(self.value)
			weight = self.weights[i]
			total += output * weight
		return total

	def valid(self):
		output = self.compute()
		thresh = self.threshold
		return output >= thresh

	def __call__(self, value):
		prev = self.get()
		self.set(value)
		if not self.valid():
			self.set(prev)
			return False
		return True