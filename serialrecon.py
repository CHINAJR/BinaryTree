class Node:
	def __init__(self,val):
		self.lchild = None
		self.rchild = None
		self.value = val

def serialByPre(head):
	if head == None:
		return '#!'
	result = str(head.value) + '!'
	result += serialByPre(head.lchild)
	result += serialByPre(head.rchild)
	return result

def reconByPreString(prestr):
	prestr1 = prestr.split('!')
	#print(prestr1)
	prestr2 = []
	for i in range(len(prestr1)):
		prestr2.append(prestr1[i])
	return reconPreOrder(prestr2)

def reconPreOrder(lists):
	a = lists.pop(0)
	if a == "#":
		return None
	head = Node(int(a))
	head.lchild = reconPreOrder(lists)
	head.rchild = reconPreOrder(lists)
	return head

if __name__ == '__main__':
	head =Node(100)
	head.lchild =Node(21)
	head.lchild.lchild =Node(37)
	head.rchild =Node(-42)
	head.rchild.lchild =Node(0)
	head.rchild.rchild =Node(666)
	pre = serialByPre(head)
	print(pre)
	pre = str(pre)
	h = reconByPreString(pre)
	pre = serialByPre(h)
	print(pre)
