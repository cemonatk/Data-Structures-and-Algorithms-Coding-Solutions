    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pointer1 = head
        pointer2 = head
        
        while (pointer2.val != None and pointer2.next != None):
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            if pointer2 != None:
                pointer2 = pointer2.next
            
        print("Mid element:")
        print(pointer1.val)
