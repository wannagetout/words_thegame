class Player:

	def __init__(self, name: str):
		self.name = name
		self.used_words_list = []

	def used_words(self):
		return len(self.used_words_list)

	def add_word(self, word):
		self.used_words_list.append(word)

	def word_check(self, word):
		return True if word in self.used_words_list else False

	def __repr__(self):
		return f"Пользователь {self.name}. Количество отгаданных слов: {len(self.used_words_list)}"