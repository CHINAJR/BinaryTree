class Node:
	def __init__(self,val):
		self.lchild = None
		self.rchild = None
		self.value = val
		self.parent = None


def getSuccessorNode(head):
	'''中序时后继节点'''
	if head == None:
		return None
	if head.rchild != None:
		return getlchildMose(head.rchild)
	else:
		parent = head.parent
		while parent != None and parent.lchild != head:
			head = parent
			parent = head.parent
		return parent

def getlchildMose(head):
	if head == None:
		return head
	while head.lchild != None:
		head = head.lchild
	return head

if __name__ == '__main__':
	head =Node(6)
	head.parent = None
	head.lchild =Node(3)
	head.lchild.parent = head
	head.lchild.lchild =Node(1)
	head.lchild.lchild.parent = head.lchild
	head.lchild.lchild.rchild =Node(2)
	head.lchild.lchild.rchild.parent = head.lchild.lchild
	head.lchild.rchild =Node(4)
	head.lchild.rchild.parent = head.lchild
	head.lchild.rchild.rchild =Node(5)
	head.lchild.rchild.rchild.parent = head.lchild.rchild
	head.rchild =Node(9)
	head.rchild.parent = head
	head.rchild.lchild =Node(8)
	head.rchild.lchild.parent = head.rchild
	head.rchild.lchild.lchild =Node(7)
	head.rchild.lchild.lchild.parent = head.rchild.lchild
	head.rchild.rchild =Node(10)
	head.rchild.rchild.parent = head.rchild	
	test = head.lchild.lchild
	print('[%d]:[%d]'%(test.value,getSuccessorNode(test).value))
	test = head.lchild.lchild.rchild
	print('[%d]:[%d]'%(test.value,getSuccessorNode(test).value))
	test = head.lchild
	print('[%d]:[%d]'%(test.value,getSuccessorNode(test).value))
	test = head.lchild.rchild
	print('[%d]:[%d]'%(test.value,getSuccessorNode(test).value))
	test = head.lchild.rchild.rchild
	print('[%d]:[%d]'%(test.value,getSuccessorNode(test).value))
	test = head
	print('[%d]:[%d]'%(test.value,getSuccessorNode(test).value))
	test = head.rchild.lchild.lchild
	print('[%d]:[%d]'%(test.value,getSuccessorNode(test).value))
	test = head.rchild.lchild
	print('[%d]:[%d]'%(test.value,getSuccessorNode(test).value))
	test = head.rchild
	print('[%d]:[%d]'%(test.value,getSuccessorNode(test).value))
	test = head.rchild.rchild
	print('[%d]:%s'%(test.value,getSuccessorNode(test)))

	
