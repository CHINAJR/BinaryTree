def mintrees(head):
	'''生成最小树'''
	v = [0] * (VERTS+1)
	ptr = head 
	while ptr != None:
		mceprt = findmincost(head)
		v[mceprt.start] += 1
		v[mceprt.to] += 1
		if v[mceprt.start] >1 and v[mceprt.to] >1:
			v[mceprt.start] -= 1
			v[mceprt.to] -= 1
		else:
			print('start[%d],end:[%d],value:[%d]'%(mceprt.start,mceprt.to,mceprt.val))
		ptr = ptr.next

def findmincost(head):
	'''寻找最小边'''
	minval = 100
	ptr = head 
	while ptr != None:
		if ptr.val < minval and ptr.find == 0:
			minval = ptr.val
			retptr = ptr
		ptr = ptr.next
	retptr.find = 1
	return retptr

class Edge:
	def __init__(self):
		self.start = 0 
		self.to = 0 
		self.val = 0
		self.find = 0 
		self.next = None

if __name__ == '__main__':
	data=[[1,2,6],[1,6,12],[1,5,10],
	[2,3,3],[2,4,5],[2,6,8],
	[3,4,7],[4,6,11],[4,5,9],
	[5,6,16]]
	VERTS = 6
	head = None
	for i in range(10):
		for j in range(1,VERTS+1):
			if data[i][0] == j:
				newnode = Edge()
				newnode.start = data[i][0]
				newnode.to = data[i][1]
				newnode.val = data[i][2]
				if head == None:
					head = newnode
					head.next = None
					ptr = head
				else:
					ptr.next = newnode
					ptr = ptr.next
	mintrees(head)

	
