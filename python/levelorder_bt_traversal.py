class Node:
	def __init__(self ,value):
		self.data = value
		self.left = None
		self.right = None

def levelOrder(root):
	if root:
		queue = [root]

		while(len(queue) > 0):
			print(queue[0].data)
			node = queue.pop(0)

			if node.left:
				queue.insert(len(queue), node.left)
			
			if node.right:
				queue.insert(len(queue), node.right)
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


levelOrder(root)
