	def reverse(self):
		prev = None
		curr = self.head

		while(curr is not None):
			next_ = curr.next
			curr.next = prev
			prev = curr
			curr = next_
		self.head = prev
		
	'''
	class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reversed_ll = ListNode() 
        stack = []
        
        node = head
        
        while node != None:
            stack.append(node)
            node = node.next
        
        for item in stack:
            reversed_ll = item
            reversed_ll = reversed.next
            
        return reversed_ll
	'''
