from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

from random import randint

import numpy as np
import re

DEFAULT_ROW  = 9
DEFAULT_COL  = 9
DEFAULT_MINE = 9
MINE = 100

class Board(GridLayout):
	"""docstring for Board"""
	
	def __init__(self, **kwargs):
		super(Board, self).__init__(**kwargs)

		self.cols = 1

		# Create rows, cols, mines layout
		self.input_layout = GridLayout(cols=6, rows=1)
		self.lblRow = Label(text="Rows: ", size_hint=(None, None), width = 64, height = 32)
		self.txtRow = TextInput(text="", size_hint=(None, None), width = 32, height = 32, multiline=False)
		self.lblCol = Label(text="Cols: ", size_hint=(None, None), width = 64, height = 32)
		self.txtCol = TextInput(text="", size_hint=(None, None), width = 32, height = 32, multiline=False)
		self.lblMine = Label(text="Mines: ", size_hint=(None, None), width = 64, height = 32)
		self.txtMine = TextInput(text="", size_hint=(None, None), width = 32, height = 32, multiline=False)

		self.input_layout.add_widget(self.lblRow)
		self.input_layout.add_widget(self.txtRow)
		self.input_layout.add_widget(self.lblCol)
		self.input_layout.add_widget(self.txtCol)
		self.input_layout.add_widget(self.lblMine)
		self.input_layout.add_widget(self.txtMine)
		self.add_widget(self.input_layout)

		# Create button OK
		self.Ok_layout = GridLayout(cols=1)
		self.btnOk = Button(text="Let's go!", size_hint=(0.2, None), height = 32)
		self.btnOk.bind(on_press=self.check_input)
		self.Ok_layout.add_widget(self.btnOk)
		self.add_widget(self.Ok_layout)

		# Create board layout
		
	def genMines(self, rows, cols, mines):
		result = [[0 for i in range(rows)] for j in range(cols)]
		# Generate mines
		arr_mines = []
		while len(arr_mines) != mines:
			x = randint(0, rows-1)
			y = randint(0, cols-1)
			if [x, y] not in arr_mines:
				arr_mines.append([x, y])
		# Add mines into board
		for x, y in arr_mines:
			result[x][y] = MINE

		# Add numbers around the mines
		getNeighbour = lambda x, y: [[x-1,y-1],	[x-1, y], [x-1, y+1],
									 [x, y+1], [x+1, y+1], [x+1, y],
									 [x+1, y-1], [x, y-1]]
		
		get_num_of_mine = lambda a, x, y: sum([1 for i, j in getNeighbour(x, y) if a[i][j] == MINE])

		tmp_r = np.pad(result, pad_width=1, mode='constant', constant_values=0)
		
		# Save padding position
		padd = [[0, y] for y in range(cols+2)]
		for y in range(cols+2):
			padd.append([rows+1, y])
		for x in range(rows+2):
			padd.append([x, 0])
			padd.append([x, cols+1])

		# Calc number of mines around the mines
		for x, y in arr_mines:
			arr_nei = getNeighbour(x, y)
			# Because we add padding => we need to map pos from original to padding by plus 1
			for i, j in arr_nei:
				if (tmp_r[i+1][j+1] == 0) and ([i+1, j+1] not in padd) and (tmp_r[i+1][j+1] != MINE):
					tmp_r[i+1][j+1] = get_num_of_mine(tmp_r, i+1, j+1)
			
		ret = []
		for e in tmp_r[1:-1]:
			ret.append(e[1:cols+1].tolist())
		return ret

	# Callback functions
	def check_input(self, even):
		if re.match(r'^([\s\d]+)$', str(self.txtRow.text) + str(self.txtCol.text) + str(self.txtMine.text)) == None:
			pop = Popup(title="Error!", content=Label(text="Incorrect input! Please check again!"), size_hint=(None, None), size=(200, 200))
			pop.open()
		else:
			irow = int(self.txtRow.text)
			icol = int(self.txtCol.text)
			imine = int(self.txtMine.text)
			self.board_layout = GridLayout(rows=irow, cols=icol)

			board = self.genMines(irow, icol, imine)
			for i in range(irow):
				for j in range(icol):
					btn = Button(text=str(board[i][j]))
					self.board_layout.add_widget(btn)
			self.add_widget(self.board_layout)


class SimpleKivy(App):
	"""docstring for SimpleKivy"""
	def build(self):
		return Board()

if __name__ == '__main__':
	SimpleKivy().run()
		