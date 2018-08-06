class Type:
	def __init__(self,m,h):
		self.m = m 
		self.h = h 

class Node(object):
	def __init__(self,elem=-1,lchild=None,rchild=None):
		self.elem = elem
		self.left = lchild
		self.right = rchild

def maxDistance(head):
	if head == None:
		ab = Type(0,0)		
		return ab
	left = maxDistance(head.left)
	right = maxDistance(head.right)
	includeHeadDistance = left.h + 1 + right.h
	p1 = left.m
	p2 = right.m
	res = max(max(p1,p2),includeHeadDistance)
	hit = max(left.h,right.h)+1
	aa = Type(res,hit)
	return  aa


if __name__ == '__main__':

	head1 = Node(1)
	head1.left = Node(2)
	head1.right = Node(3)
	head1.left.left = Node(4)
	head1.left.right = Node(5)
	head1.right.left = Node(6)
	head1.right.right = Node(7)
	head1.left.left.left = Node(8)
	head1.right.left.right = Node(9)
	print(maxDistance(head1).m)

	head2 = Node(1)
	head2.left = Node(2)
	head2.right = Node(3)
	head2.right.left = Node(4)
	head2.right.right = Node(5)
	head2.right.left.left = Node(6)
	head2.right.right.right = Node(7)
	head2.right.left.left.left = Node(8)
	head2.right.right.right.right = Node(9)
	print(maxDistance(head2).m)
