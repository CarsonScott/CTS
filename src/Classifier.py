def classify(patterns, input):
	scores = []
	for i in range(len(patterns)):
		score = 0
		size = 0
		for y in range(len(patterns[i])):
			for x in range(len(patterns[i][y])):
				value = patterns[i][y][x]
				reference = input[y][x]
				score += value == reference
				size += 1
		score /= size
		scores.append(score)
	return scores.index(max(scores))

class Classifier:
	def __init__(self, patterns):
		self.patterns = patterns
	def __call__(self, input):
		return classify(self.patterns, input)
