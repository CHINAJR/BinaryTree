class Node:
	def __init__(self,val):
		self.val = val
		self.lchild = None
		self.rchild = None


#recursive 递归
def preorderRecur(root):
	if root == None:
		return 
	print(root.val,end=' ')
	preorderRecur(root.lchild)
	preorderRecur(root.rchild)

def inorderRecur(root):
	if root == None:
		return 
	inorderRecur(root.lchild)
	print(root.val,end=' ')
	inorderRecur(root.rchild)

def postorderRecur(root):
	if root == None:
		return 
	postorderRecur(root.lchild)
	postorderRecur(root.rchild)
	print(root.val,end=' ')

#unrecrsive 非递归
def preorderUnRecur(root):
	if root == None:
		return
	lists = []
	lists.append(root)
	while(len(lists) != 0):
		root = lists.pop()
		print(root.val,end=' ')
		if root.rchild != None:
			lists.append(root.rchild)
		#break
		if root.lchild != None:
			lists.append(root.lchild)

def inorderUnRecur(root):
	if root == None:
		return
	lists = []
	while root != None or len(lists):
		if root != None:
			lists.append(root)
			root = root.lchild
		else:
			root = lists.pop()
			print(root.val,end=' ')
			root = root.rchild

def posterUnRecur(root):
	if root == None:
		return
	lists = []
	list2 = []
	lists.append(root)
	while len(lists):
		root = lists.pop()
		list2.append(root)
		if root.lchild != None:
			lists.append(root.lchild)
		if root.rchild != None:
			lists.append(root.rchild)
	while len(list2):
		print(list2.pop().val,end=' ')

if __name__ == '__main__':
	head = Node(5)
	head.lchild = Node(3)
	head.rchild = Node(8)
	head.lchild.lchild = Node(2)
	head.lchild.rchild = Node(4)
	head.lchild.lchild.lchild = Node(1)
	head.rchild.lchild = Node(7)
	head.rchild.lchild.lchild = Node(6)
	head.rchild.rchild = Node(10)
	head.rchild.rchild.lchild = Node(9)
	head.rchild.rchild.rchild = Node(11)

	preorderRecur(head)
	print('')
	inorderRecur(head)
	print('')
	postorderRecur(head)
	print('')
	preorderUnRecur(head)
	print('')
	inorderUnRecur(head)
	print('')
	posterUnRecur(head)
	print('')

	
