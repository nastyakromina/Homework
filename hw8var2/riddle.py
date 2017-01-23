import random

def get_words(fn):
#Функция записывает загадываемое слово в ключ, а подсказки к этому слову с многоточиями - в значение
	words = {}
	with open(fn, 'r') as fd:
		for line in fd:
			word, collocations = line.split(',', 1)
			words[word] = collocations.replace(word, '.'*len(word)).split(',')
	return words

def ask_riddle(words_dict):
#Функция загадывает слово из словаря и выдает подсказку пользователю
	words = list(words_dict.keys())
	rnd_word = random.choice(words)
	rnd_collocation = random.choice(list(words_dict[rnd_word]))
	print(rnd_collocation)
	word = input('Пропущенное слово:')
	return rnd_word, word == rnd_word

def main():
#Главная функция
	words = get_words('f3.csv')
	word, answer = ask_riddle(words)
	print('И это правильный ответ!' if answer else 'Вы ошиблись, правильный ответ: '+ word)
	return word, answer
main()
