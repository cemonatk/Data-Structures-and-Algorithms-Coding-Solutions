# Validate BST or not

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def isBSTUtil(node, mini, maxi):
	if node is None:
		return True
	
	if node.data < mini or node.data > maxi:
		return False

	return isBSTUtil(node.left, mini, node.data) and isBSTUtil(node.right, node.data, maxi)

def isBST(node):
	return isBSTUtil(node, float("-inf"), float("inf"))

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

print(isBST(root))
