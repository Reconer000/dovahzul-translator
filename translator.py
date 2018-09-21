'''
___________________________
Dovahzul translator

install included font to see glyphs

Made by Reconer_000
___________________________
'''
import ui
import clipboard
from console import hud_alert
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


def copy_action(sender):
	clipboard.set(sender.superview['textview1'].text)
	hud_alert('Copied')


def translate(text, dictionary, filler=None):
	return ' '.join(
		[dictionary.get(word, filler or word) for word in text.split()])


def dte(sender):
	words = capwords(sender.text).split()
	v['textview1'].text = ""
	v['textview2'].text = ""
	for obj in words:
		v['textview2'].text += obj.lower() + '   '
		v['textview1'].text += " " + translate(obj, dovahzul_to_english, filler='?')
	v['words1'].text = ""


def etd(sender):
	words = capwords(sender.text).split()
	v['textview1'].text = ""
	v['textview2'].text = ""
	for obj in words:
		obj = strip_right(obj, suffix)
		kek = translate(obj, english_to_dovahzul, filler='?')
		v['textview1'].text += kek + ' '
		v['textview2'].text += kek.lower() + '   '
	v['words'].text = ""


v = ui.load_view('translator')
if ui.get_screen_size()[1] >= 768:
	# iPad
	v.present('sheet')
else:
	# iPhone
	v.present()
