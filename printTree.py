class Node(object):
	def __init__(self,elem=-1,lchild=None,rchild=None):
		self.elem = elem
		self.lchild = lchild
		self.rchild = rchild

def printTree(root):
    print("Binary Tree:")
    printInOrder(root, 0, 'H', 17)
    
def printInOrder(root, height, s, length):
    if root is None:
        return
    printInOrder(root.rchild, height + 1, 'v', length)
    val = s + str(root.elem) + s
    lenM = len(val)
    lenL = (length - lenM) // 2
    lenR = length - lenM -lenL
    val = getSpace(lenL) + val + getSpace(lenR)
    print(getSpace(height * length) +val)
    printInOrder(root.lchild, height + 1, '^', length)

def getSpace(num):
    return ' ' * num

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
				if cur.elem != 'None':
					if cur.lchild == None:
						cur.lchild = node
						return
					elif cur.rchild == None:
						cur.rchild = node
						return
					else:
						queue.append(cur.lchild)
						queue.append(cur.rchild)

		    
if __name__ == "__main__":
	print(' ' * 8)
	tree = Tree()
	tree.add(0)
	tree.add(1)
	tree.add('None')
	tree.add(3)
	tree.add(4)
	tree.add(5)
	tree.add(6)
	tree.add(7)
	tree.add(8)
	tree.add(9)
	printTree(tree.root)
