class Node:
	def __init__(self,val):
		self.left = None
		self.right = None
		self.val = val 

def isBalance(head):
	res = True
	getHeight(head,1,res)
	return res

def getHeight(head,level,res):
	if head == None:
		return level
	lh = getHeight(head.left,level+1,res)
	if res != True:
		return level
	rh = getHeight(head.right,level+1,res)
	if res != True:
		return level
	if abs(lh-rh) > 1:
		res = False
	return max(lh,rh)

if __name__ == '__main__':
	head = Node(1)
	head.lchild = Node(2)
	head.rchild = Node(3)
	head.lchild.lchild = Node(4)
	head.lchild.rchild = Node(5)
	head.rchild.lchild = Node(6)
	print(isBalance(head))
