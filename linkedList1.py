class LinkedList:


	class _Node:
		__slots__ = '_element', '_next'

		def __init__(self,element,next):
			self._element = element
			self._next = next

	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size
	def is_empty(self):
		return self._size == 0

	def add_first(self,e):
		newest = self._Node(e,None)
		if self.is_empty():
			self._head = newest
			self._tail = newest
		else:
			newest._next = self._head
		self._head = newest
		self._size += 1

	def add_last(self,e):
		newest = self._Node(e,None)
		if self.is_empty():
			self._head = newest
			self._tail = newest
		else:
			self._tail._next = newest
		self._tail = newest
		self._size  += 1

	def add_any(self,e,pos):
		newest =self._Node(e,None)
		thead =self._head
		i = 1
		while i < pos:
			thead = thead._next
			i += 1
		newest._next = thead._next
		thead._next = newest
		self._size += 1

	def remove_first(self):
		if self.is_empty():
			return True
		value = self._head._element
		self._head =self._head._next
		self._size -= 1
		if self.is_empty():
			self._tail =None
		return value

	def remove_last(self):
		if self.is_empty():
			return True
		thead = self._head
		i = 0
		while i<len(self)-2:
			thead = thead._next
			i+=1
		self._tail = thead
		thead = thead._next
		value = thead._element
		self._tail._next=None
		self._size -= 1
		return value

	def remove_any(self,pos):
		if self.is_empty():
			return True
		thead = self._head
		i=1
		while i<pos-1:
			thead=thead._next
			i += 1
		value = thead._next._element
		thead._next = thead._next._next
		self._size -= 1
		return value

	def display(self):
		thead = self._head
		while thead:
			print(thead._element,end='-->')
			thead = thead._next
		print()



L=LinkedList()
L.add_first(10)
L.add_first(20)
L.add_first(30)
L.display()
L.add_last(100)
L.add_any('Rahul',3)
L.display()
L.remove_any(2)
L.display()