#!python2
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
import translator as t


def copy(sender):
	clipboard.set(v['textview1'].text)
	hud_alert('Copied')
	ui.end_editing()


def hide_keyboard(self):
	ui.end_editing()


def clear(self):
	v['words'].text = ''
	v['textview1'].text = ''
	v['textview2'].text = ''


def dte(sender):
	text = v['words'].text
	clear('kek')
	v['textview1'].text += t.dte(text)


def etd(sender):
	text = v['words'].text
	clear('kek')
	v['textview1'].text += t.etd(text)
	v['textview2'].text += t.spechar(t.etd(text))


v = ui.load_view('translator')
v.present('sheet', title_bar_color='#4fa1ae')

