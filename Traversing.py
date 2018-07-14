class Node(object):
	def __init__(self,elem=-1,lchild=None,rchild=None):
		self.elem = elem
		self.lchild = lchild
		self.rchild = rchild


class Tree(object):
	def __init__(self,root=None):
		self.root = None

	def add(self,elem):
		node = Node(elem)
		if self.root == None:
			self.root = node
		else:
			queue = []
			queue.append(self.root)
			while queue:
				cur = queue.pop(0)
				if cur.lchild == None:
					cur.lchild = node
					return
				elif cur.rchild == None:
					cur.rchild = node
					return
				else:
					queue.append(cur.lchild)
					queue.append(cur.rchild)

	def preorder(self,root):
		'''先序'''
		if root == None:
			return 
		print(root.elem,end=' ')
		self.preorder(root.lchild)
		self.preorder(root.rchild)


	def inorder(self,root):
		'''中序'''
		if root == None:
			return
		self.inorder(root.lchild)
		print(root.elem,end=' ')
		self.inorder(root.rchild)
		

	def postorder(self,root):
		'''后序'''
		if root == None:
			return
		self.postorder(root.lchild)
		self.postorder(root.rchild)
		print(root.elem,end=' ')

	def breadth_travel(self,root):
		'''层次'''
		if root == None:
			return
		queue = []
		queue.append(root)
		while queue:
			node = queue.pop(0)
			print(node.elem,end=' ')
			if node.lchild != None:
				queue.append(node.lchild)
			if node.rchild != None:
				queue.append(node.rchild)
		    
if __name__ == "__main__":
	tree = Tree()
	tree.add(0)
	tree.add(1)
	tree.add(2)
	tree.add(3)
	tree.add(4)
	tree.add(5)
	tree.add(6)
	tree.add(7)
	tree.add(8)
	tree.add(9)
	tree.preorder(tree.root)
	print()
	tree.inorder(tree.root)
	print()
	tree.postorder(tree.root)
	print()
	tree.breadth_travel(tree.root)



