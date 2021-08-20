	def reverse(self):
		prev = None
		curr = self.head

		while(curr is not None):
			next_ = curr.next
			curr.next = prev
			prev = curr
			curr = next_
		self.head = prev
