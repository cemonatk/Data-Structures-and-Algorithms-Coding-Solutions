
'''
Inorder (Left, Root, Right)
Preorder (Root, Left, Right
Postorder (Left, Right, Root)
'''

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def preorder(root):
	if root:
		print(root.val)
		
		printPreorder(root.left)
		
		printPreorder(root.right)
		

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preorder(root)
