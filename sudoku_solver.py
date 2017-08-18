import random

class Grid(object):
	def __init__(self, grid=[]):
		self.grid = grid		

		if not self.grid:
			self.grid = [[0] * 9 for i in range(9)]

	def at(self, x, y):
		return self.grid[y][x]

	def set(self, x, y, val):
		self.grid[y][x] = val

	def __str__(self):
		s = ""
		for i, row in enumerate(self.grid):
			for j, cell in enumerate(row):
				s += str(cell)
				if (j + 1) % 3 == 0 and j != 8: s += '|'
			s += '\n'
			if (i + 1) % 3 == 0 and i != 8:
				s += (("-" * 3) + '+') * 3
				s = s[:-1]
				s += '\n'

		s = s[:-1]

		return s
	
	def print(self):
		print(str(self))

	@staticmethod
	def random():
		return Grid([[random.randint(1, 9) for j in range(9)] for i in range(9)])		

	def copy(self):
		return Grid([row[:] for row in self.grid])

	def get_row(self, y):
		return self.grid[y]

	def get_column(self, x):
		return [self.at(x, y) for y in range(9)]	

	def get_square(self, x, y):
		square = (int(x / 3), int(y / 3))	
		return [self.at(i, j) for i in range(square[0] * 3, square[0] * 3 + 3) for j in range(square[1] * 3, square[1] * 3 + 3)]

	def get_candidates(self, x, y):
		row = set(self.get_row(y))
		column = set(self.get_column(x))
		square = set(self.get_square(x, y))

		candidates = {1, 2, 3, 4, 5, 6, 7, 8, 9}
		candidates = candidates.difference(row)
		candidates = candidates.difference(column)
		candidates = candidates.difference(square)

		return sorted(list(candidates))

	def is_solved(self):
		return all([all(row) for row in self.grid])

	def solve(self, depth=0):
		if self.is_solved(): 
			return self
		
		for x in range(9):
			for y in range(9):
				cell = self.at(x, y)
				if not cell:		
					cands = self.get_candidates(x, y)	
					for cand in cands:
						gp = self.copy()
						gp.set(x, y, cand)
						gp = gp.solve(depth + 1)
						if gp: return gp		
					return None

def test():
	sfile = open('test.txt', 'r')
	grid = [list(map(int, sfile.readline()[:-1])) for i in range(9)]	
	sfile.close()

	grid = Grid(grid)

	grid.print()

	grid = grid.solve()

	grid.print()

