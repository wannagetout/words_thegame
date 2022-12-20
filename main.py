from base_word import BasicWord
from players import Player
from utils import get_random_word


def app():
	print("Добро пожаловать в игру \"Слова\"")
	user_name = input("Представьтесь, пожалуйста: ")
	user = Player(user_name)
	print(f"Привет {user.name}")
	word = get_random_word()
	print(f"Составьте {len(word.subwords)} слов из слова {word.word}")
	print("Слова не должны быть короче 3 букв")
	print("Чтобы закончить игру, угадайте все слова илии введите \"stop\"")

	print("Поехали. Ваше первое слово: ")
	while len(user.used_words_list) <= len(word.subwords):
		user_word = input().lower()
		if user_word == "stop" or user_word == "стоп":
			break
		if len(user_word) > 2:
			if user_word in word.subwords:
				if user_word not in user.used_words_list:
					print("Верно!")
					user.used_words_list.append(user_word)
				else:
					print("Это слово уже отгадано")
			else:
				print("неверно")
		else:
			print("Слишком короткое слово!")
	print(f"Игра завершена. Вы угадали {len(user.used_words_list)} слов!")


if __name__ == "__main__":
	app()

