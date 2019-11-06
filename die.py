
from roll_result import RollResult
from random import randint

class Die (object):
	
	def __init__(self, sides=None, faces=None):
		self._held = False
		self._cur_face_idx = 0
		self._last_result = None
		
		if sides and type(sides) is int:
			if sides >= 2:
				self._faces = range(1, sides + 1)
			else:
				raise ValueError('A Die must have 2 or more sides: %s given.' % sides)
		elif faces and type(faces) is list:
			if len(faces) >= 2:
				self._faces = faces
			else:
				raise ValueError('Provided list of faces must have at least 2 entries: %s given.' % faces)
		else:
			raise TypeError('Please provide the number of sides on the die, or a list of face values')
			
			
	## properties
			
	@property
	def faces(self):
		return self._faces
		
	@property
	def sides(self):
		return len(self._faces)
		
	@property
	def value(self):
		return self._faces[self._cur_face_idx]
		
	@value.setter
	def value(self, val):
		try:
			self._cur_face_idx = self.faces.index(val)
		except Exception as ex:
			raise Exception('This die doesnt have a face with a value of %s. Faces: %s' % (val, self.faces))
			
	@property
	def held(self):
		return self._held
		
	@property
	def last_result(self):
		return self._last_result
		
		
	## public
		
	def hold(self):
		self._held = True
		
	def toggle_hold(self):
		self._held = not self.held
		return self.held
		
	def release(self):
		self._held = False
		
	def roll(self):
		if not self.held:
			self._cur_face_idx = randint(0, self.sides - 1)
			self._last_result = RollResult([self.sides])
		return self.value
		

if __name__ == '__main__':
	d = Die(6)
	d.value = 4
	print(d.value)
	
	try:
		d.value = 6
	except Exception as ex:
		print(ex)
