class Node:
	def __init__(self,val):
		self.lchild = None
		self.rchild = None
		self.val = val 
def isCBT(head):
	leaf = False
	if head == None:
		return True
	lists = []
	lists.append(head)
	while len(lists):
		head = lists.pop(0)
		if (head.rchild != None and head.lchild == None)or\
		(leaf and (head.lchild != None or head.rchild != None)):
			return False
		if head.lchild != None:
			lists.append(head.lchild)
		if head.rchild != None:
			lists.append(head.rchild)
		else:
			leaf = True
	return True

if __name__ == '__main__':
	head = Node(1)
	head.lchild = Node(2)
	head.rchild = Node(3)
	head.lchild.lchild = Node(4)
	head.lchild.rchild = Node(5)
	head.rchild.lchild = Node(6)
	print(isCBT(head))	
