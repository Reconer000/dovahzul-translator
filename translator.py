#!python2
import csv
from string import capwords
#add ', encoding="utf-8"' after mode='r' for python3 use
with open('dovah.csv', mode='r') as infile:
	reader = csv.reader(infile)
	english_to_dovahzul = dict((rows[0], rows[1]) for rows in reader)

dovahzul_to_english = {v: k for k, v in english_to_dovahzul.items()}

prefixes = {'non': 'ni', 're': 'or', 'dis': 'vo', 'un': 'vo'}

suffixes = {
	'ing': 'von',
	's': 'he',
	'ship': 'dein',
	'ly': 'gaar',
	'er': 'iik',
	'ous': 'kei',
	'less': 'nu',
	'ness': 'om',
	'ism': 'un',
	'y': 'us'
}

specialchars = {
	'ah': 'H',
	'aa': 'A',
	'ei': 'W',
	'ey': 'E',
	'ii': 'I',
	'ir': 'J',
	'oo': 'O',
	'uu': 'U',
	'ur': 'R',
}


def suffix(text, dictionary):
	if dictionary == english_to_dovahzul:
		for x, y in suffixes.items():
			text = text.replace(x, ' ' + x)
	else:
		for x, y in suffixes.items():
			text = text.replace(y, ' ' + y)
	text = translate(text, dictionary, filler='?')
	return text.replace(' ', '')


def prefix(text, dictionary):
	if dictionary == english_to_dovahzul:
		for x, y in prefixes.items():
			text = text.replace(x, ' ' + x)
	else:
		for x, y in suffixes.items():
			text = text.replace(y, ' ' + y)
	text = translate(text, dictionary, filler='?')
	return text.replace(' ', '')


def spechar(text):
	for x, y in specialchars.items():
		text = text.replace(x, y)
	return text


def translate(text, dictionary, filler=None):
	text = ' '.join(
		[dictionary.get(word, filler or word) for word in text.split()])
	return text


def dte(text):
	rtn = ''
	words = capwords(text).split()
	for obj in words:
		kek = translate(obj, dovahzul_to_english, filler='?')
		if kek == '?':
			kek = suffix(obj, dovahzul_to_english)
			if kek == '?':
				kek = prefix(obj, dovahzul_to_english)
		rtn += kek.lower() + ' '
	return rtn


def etd(text):
	rtn = ''
	words = capwords(text).split()
	for obj in words:
		kek = translate(obj, english_to_dovahzul, filler='?')
		if kek == '?':
			kek = suffix(obj, english_to_dovahzul)
		rtn += kek.lower() + ' '
	return rtn

