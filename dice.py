
from roll_result import RollResult
from die import Die

class Dice (object):
	
	def __init__(self, num_dice=None, num_sides=None, std_die_dict=None):
		self._dice = []
		self._cur_total = 0
		if std_die_dict and type(std_die_dict) is dict:
			for key, val in std_die_dict.items():
				if type(key) is int and type(val) is int:
					for _ in range(key):
						self._dice += [Die(val)]
		elif num_dice and num_sides and type(num_dice) is int and type(num_sides) is int:
			for _ in range(num_dice):
				self._dice += [Die(num_sides)]
				
		self._cur_total = self._calc_total()
		
	def __iter__(self):
		return (die for die in self._dice)
		
	def __getitem__(self, i):
		return self._dice[i]
		
	def __len__(self):
		return len(self._dice)
		
	
	## properties
		
	@property
	def dice(self):
		return self._dice
		
	@property
	def num_dice(self):
		return len(self._dice)
		
	@property
	def values(self):
		vals = []
		for die in self._dice:
			vals += [die.value]
		return vals
		
	@values.setter
	def values(self, vals):
		if type(vals) == list and len(vals) == self.num_dice:
			for i,die in enumerate(self._dice):
				die.value = vals[i]
		else:
			raise TypeError('Given values must be a list of values with as many entries as there are dice. Values: %s; num dice: %s' % (vals, self.num_dice))
		
	@property
	def value(self):
		return self._cur_total
		
		
	## private
	
	def _calc_total(self):
		return sum(self.values)
		
		
	## public
		
	def hold_all(self):
		for die in self._dice:
			die.hold()
			
	def release_all(self):
		for die in self._dice:
			die.release()
			
	def held(self, idx):
		return self._dice[idx].held
			
	def hold(self, idx):
		self._dice[idx].hold()
		
	def toggle_hold(self, idx):
		return self._dice[idx].toggle_hold()
	
	def release(self, idx):
		self._dice[idx].release()
		
	def add(self, die):
		if type(die) is Die:
			self._dice += [die]
			self._cur_total += die.value
		else:
			raise TypeError('Can only add a Die to a group of Dice')
			
	def roll(self):
		for die in self._dice:
			die.roll()
		self._cur_total = self._calc_total()
		return self.value
