class Node:
	def __init__(self,val):
		self.lchild = None
		self.rchild = None
		self.val = val 
def nodeNum(head):
	if head == None:
		return 0 
	h1 = mostlchildLevel(head,1)
	if h1 == 1:
		return 1
	h2 = 1
	if head.rchild != None:
		h2 = mostlchildLevel(head.rchild,2)
	if h2 == h1:
		return pow(2,h1-1)+nodeNum(head.rchild)
	else:
		return pow(2,h2-1)+nodeNum(head.lchild)

def mostlchildLevel(head,l):
	while head.lchild != None:
		head = head.lchild
		l = l+1	
	return l

if __name__ == '__main__':
	head = Node(1)
	head.lchild = Node(2)
	head.rchild = Node(3)
	head.lchild.lchild = Node(4)
	head.lchild.rchild = Node(5)
	head.rchild.lchild = Node(6)
	a = nodeNum(head)
	print(a)
