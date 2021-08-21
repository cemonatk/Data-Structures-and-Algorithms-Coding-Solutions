# levelordertraversal
class Queue(object):
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []
	
	def enqueue(self, item):
		self.items.insert(0, item)
	
	def dequeue(self):
		return self.items.pop()
	
	def size(self):
		return len(self.items)

	def peek(self):
		if not self.isEmpty():
			return self.items[-1]
		else:
			raise Exception('It is empty.')
	
	def size(self):
		return len(self.items)

queue = Queue()
queue.enqueue(1)
