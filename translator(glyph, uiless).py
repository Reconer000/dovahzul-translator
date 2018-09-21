'''
___________________________
Dovahzul translator (without ui)

install included font to see glyphs

Made by Reconer_000
___________________________
'''
import csv
from string import capwords
import sys, os, console

with open('dovah.csv', mode='r', encoding="utf-8") as infile:
	reader = csv.reader(infile)
	english_to_dovahzul = dict((rows[0], rows[1]) for rows in reader)

dovahzul_to_english = {v: k for k, v in english_to_dovahzul.items()}

suffix = 's', 'ing', 'es'
prefix = ' '
glyph = ('Dragon_Alphabet_Private', 12)
fnt = ('Menlo', 12)

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
	console.set_font(*glyph)
	words = capwords(input).split()
	for obj in words:
		kek = translate(obj, english_to_dovahzul, filler='?')
		console.set_font(*glyph)
		print(kek.lower(), end = '   ')
	console.set_font(*fnt)

console.set_font(*fnt)
print('Enter dte for Dovahzul to English, or etd for english to dovahzul.')
direction = input()

print('Now enter the text you want to translate.')
input = input()

if direction == 'dte':
	dte(input)
else:
	etd(input)
