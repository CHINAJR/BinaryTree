class Node:
	def __init__(self,val):
		self.lchild = None
		self.rchild = None
		self.val = val 

def inorderUnrecur(head):
	if head == None:
		return 
	lists = []
	pre = 0
	while head != None or len(lists):
		if head != None:
			lists.append(head)
			head = head.lchild
		else:
			head = lists.pop()
			if pre < head.val:
				pre = head.val
				head = head.rchild
			else:
				return False
	return True

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

	print(inorderUnrecur(head))
