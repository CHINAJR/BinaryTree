def paperfold(N):
	printprocess(1,N,True)

def printprocess(i,N,down):
	'''纸向上对折可等价中序'''
	if i > N:
		return
	printprocess(i+1,N,True)
	print(down)
	printprocess(i+1,N,False)

if __name__ == '__main__':
	N = 4
	paperfold(4)
