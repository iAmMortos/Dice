
class RollResult (object):
	def __init__(self, faces=[]):
		self._faces = faces
		
	@property
	def faces(self):
		return self._faces[::]
		
	@property
	def total(self):
		t = 0
		for face in self._faces:
			try:
				round(face)
				t += face
			except:
				raise Exception('Not all faces are numeric. Cannot sum roll.')
		return t
