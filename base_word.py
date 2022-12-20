class BasicWord:
	def __init__(self, word, subwords):
		self.word = word
		self.subwords = subwords


	def check_subword(self, subword, subwords):
		return True if subword in subwords else False

	def count_subwords(self, subwords):
		return len(subwords.split(" "))

	def __repr__(self):
		return f"Слово: {self.word}. Количество возможных слов: {len((self.subwords).split(' '))}"

