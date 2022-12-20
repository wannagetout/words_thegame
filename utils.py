import requests
import json
from random import randint
from base_word import BasicWord


def get_random_word():
	url = "https://www.jsonkeeper.com/b/7POE"
	request_json = requests.get(url)
	json_get = json.loads(request_json.text)
	word_number = randint(0, 2)
	word = json_get[word_number]['word']
	subwords = json_get[word_number]['subwords']
	word = BasicWord(word=word, subwords=subwords)
	return word
