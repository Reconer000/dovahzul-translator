'''
___________________________
Dovahzul translator (without ui/glyphs)

Made by Reconer_000
___________________________
'''
import csv
from string import capwords

with open('dovah.csv', mode='r', encoding="utf-8") as infile:
	reader = csv.reader(infile)
	english_to_dovahzul = dict((rows[0], rows[1]) for rows in reader)

dovahzul_to_english = {v: k for k, v in english_to_dovahzul.items()}

suffix = 's', 'ing', 'es'
prefix = ' '


def strip_left(text, prefix):
	if not text.startswith(prefix):
		return text
	return text[len(prefix):]


def strip_right(text, suffix):
	if not text.endswith(suffix):
		return text
	elif text.endswith('s'):
		return text[:len(text) - len('s')]
	elif text.endswith('ing'):
		return text[:len(text) - len('ing')] + "e"


def translate(text, dictionary, filler=None):
	return ' '.join(
		[dictionary.get(word, filler or word) for word in text.split()])


def dte(input):
	words = capwords(input).split()
	for obj in words:
		print(translate(obj, dovahzul_to_english, filler='?'), end=' ')


def etd(input):
	words = capwords(input).split()
	for obj in words:
		print(translate(obj, english_to_dovahzul, filler='?'), end=' ')


print('Enter dte for Dovahzul to English, or etd for english to dovahzul.')
direction = input()

print('Now enter the text you want to translate.')
input = input()

if direction == 'dte':
	dte(input)
else:
	etd(input)
