class Node(object):
	def __init__(self,elem=-1,lchild=None,rchild=None):
		self.elem = elem
		self.lchild = lchild
		self.rchild = rchild

def Morrissort(head):
	if head == None:
		return ;
	cur1 = head
	cur2 = None
	while cur1 != None:
		cur2 = cur1.lchild
		if cur2 != None:
			while cur2.rchild != None and cur2.rchild != cur1:
				cur2 = cur2.rchild
			if cur2.rchild == None:
				cur2.rchild = cur1
				cur1 = cur1.lchild
				continue
			else:
				cur2.rchild = None
				printedge(cur1.lchild)
		cur1 = cur1.rchild
	#print()
	printedge(head)

def printedge(head):
	tail = reverseEdge(head)
	cur = tail
	while cur != None:
		print(cur.elem)
		cur = cur.rchild
	reverseEdge(tail)

def reverseEdge(froms):
	pre = None
	nexts = None
	while froms != None:
		nexts = froms.rchild
		froms.rchild = pre
		pre = froms
		froms = nexts
	return pre

	

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
	Morrissort(head)
