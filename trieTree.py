class TrieNode:
	
	def __init__(self):
		self.path = 0 
		self.end = 0 
		self.nexts = [0 for i in range(26)]

class TrieTree:	
	def __init__(self):
		self.root = TrieNode()

	def insert(self,word):
		if word == None:
			return 
		index = 0 
		node = self.root
		for i in range(len(word)):
			index = ord(word[i]) - ord('a')
			if node.nexts[index] == 0:
				node.nexts[index] = TrieNode()
			node = node.nexts[index]
			node.path += 1
		node.end += 1

	def delete(self,word):
		if word == None:
			return 
		index = 0 
		node = self.root
		for i in range(len(word)):
			index = ord(word[i]) - ord('a')
			if node.nexts[index].path == 1:
				node.nexts[index].path =0
				node.nexts[index] = 0
				return
			node.nexts[index].path -= 1
			node = node.nexts[index]
		node.end -=1


	def search(self,word):
		if word == None:
			return 
		index = 0 
		node = self.root
		for i in range(len(word)):
			index = ord(word[i]) - ord('a')
			if node.nexts[index] == 0:
				return 0
			node = node.nexts[index]
		return node.end

	def prefixNumber(self,word):
		if word == None:
			return 0 
		index = 0 
		node = self.root
		for i in range(len(word)):
			index = ord(word[i]) - ord('a')
			if node.nexts[index] == 0:
				return 0 
			node = node.nexts[index]
		return node.path

if __name__ == '__main__':
		trie = TrieTree()
		print(trie.search("zuo"))
		trie.insert("zuo")
		print(trie.search("zuo"))
		trie.delete("zuo")
		print(trie.search("zuo"))
		trie.insert("zuo")
		trie.insert("zuo")
		trie.delete("zuo")
		print(trie.search("zuo"))
		trie.delete("zuo")
		print(trie.search("zuo"))
		trie.insert("zuoa")
		trie.insert("zuoac")
		trie.insert("zuoab")
		trie.insert("zuoad")
		trie.delete("zuoa")
		print(trie.search("zuoa"))
		print(trie.prefixNumber("zuo"))

	
