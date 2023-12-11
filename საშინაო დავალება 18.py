# მოიძიეთ და გაარჩიეთ (კომენტარებით) linked list _ის რომელიმე ტიპის კოდი.

# შექმნილია კლასი node, რომელიც წარმოადგენს ერთ ცალ node-ს linked list-ში და აქვს ორი ატრიბუტი. data- რომ შეინახოს node-ის data, და next.

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# შემდეგ შექმნილია კლასი LinkedList, რომელსაც აქვს ერთი ატრიბუტი - head. head-ის მნიშვნელობაა none, რაც იმას ნიშნავს, რომ სია ცარიელია.

class LinkedList:
	def __init__(self):
		self.head = None
		
# insertAtBegin ფუნქცია სიის დასაწყისში ჩასვამს ახალ node-ს მითითებული ინფორმაციით. ეს ფუნქცია ქმნის ახალ node-ს და ამოწმებს სია ცარიელია თუ არა. 
# (თუ ცარიელია ახალი node ხდება head), ხოლო თუ არ არის, head აფდეითდება და ახალი node ხდება head. 

	def insertAtBegin(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		else:
			new_node.next = self.head
			self.head = new_node

# insertAtIndex ახალ node-ს სვამს რომელიღაც კონკრეტულ ინდექსზე გადაცემული ინფორმაციით. თუ ინდექსი ნოლის ტოლია, ის იძახებს insertAtBegin-ს. თუ არადა, გაივლის სიას რომ იპოვოს node იმ კონკრეტულ ინდექსზე.
# თუ ინდექსს იპოვის, ახალი node ჩაისმება ამჟამინდელ node-სა და შემდეგ node-ს შორის. სხვა შემთხვევაში პრინტავს "Index not present."

	def insertAtIndex(self, data, index):
		new_node = Node(data)
		current_node = self.head
		position = 0
		if position == index:
			self.insertAtBegin(data)
		else:
			while(current_node != None and position+1 != index):
				position = position+1
				current_node = current_node.next

			if current_node != None:
				new_node.next = current_node.next
				current_node.next = new_node
			else:
				print("Index not present")

# insertAtEnd fფუნქცია ახალ node-ს სიის ბოლოში სვამს. თუ სია ცარიელია ახალი node ხდება head, თუ არაა, მაშინ ფუნქცია გაივლის მთელ სიას რომ იპოვოს ბოლო node და მიაბას მას ახალი node. 

	def insertAtEnd(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return

		current_node = self.head
		while(current_node.next):
			current_node = current_node.next

		current_node.next = new_node

# updateNode ააფდეითებს node-ის ინფორმაციას კონკრეტულ ინდექსზე ახალი მნიშვნელობით. თუ ინდექსი 0-ია, ეს ფუნქცია პირდაპირ ააფდეითებს head-ის მონაცემებს, 
# სხვა შემთხვევაში სიას გაივლის რომ იპოვოს ის კონკრეტული node და გაანახლოს მისი ინფორმაცია. თუ ვერ იპოვის, პრინტავს - 'Index not present.'

	def updateNode(self, val, index):
		current_node = self.head
		position = 0
		if position == index:
			current_node.data = val
		else:
			while(current_node != None and position != index):
				position = position+1
				current_node = current_node.next

			if current_node != None:
				current_node.data = val
			else:
				print("Index not present")
				
# remove_first_node სიიდან პირველ node-ს შლის. შემდეგ შეამოწმებს არის თუ არა სია ცარიელი. თუ არ არის ცარიელი, head-ს ანახლებს შემდეგ node-ით, 
# და აშორებს პირველ node-ს.

	def remove_first_node(self):
		if(self.head == None):
			return

		self.head = self.head.next

# remove_last_node ფუნქცია შლის ბოლო node-ს სიიდან. და ესეც ამოწმებს არის თუ არა სია ცარიელი. თუ არაა, გაივლის სიას, რომ იპოვოს ბოლოდან მეორე node და წაშალოს ბოლო node. 

	def remove_last_node(self):

		if self.head is None:
			return

		current_node = self.head
		while(current_node.next.next):
			current_node = current_node.next

		current_node.next = None
		
# remove_at_index შლის node-ს კონკრეტულ ინდექსზე. თუ ინდექსი ნოლის ტოლია, ის იძახებს remove_first_node-ს.თუ არადა, გაივლის სიას, რომ იპოვოს ის node კონკრეტულ 
# ინდექსზე და წაშალოს. თუ ვერ იპოვის, დაპრინტავს'Index not present'

	def remove_at_index(self, index):
		if self.head == None:
			return

		current_node = self.head
		position = 0
		if position == index:
			self.remove_first_node()
		else:
			while(current_node != None and position+1 != index):
				position = position+1
				current_node = current_node.next

			if current_node != None:
				current_node.next = current_node.next.next
			else:
				print("Index not present")

# remove_node შლის node-ს კონკრეტული მონაცემით. თუ მონაცემი head-შია, იძახებს remove_first_node-ს. სხვა შემთხვევაში, გაივლის სიას რომ იპოვოს ის რაც უნდა და წაშალოს. 

	def remove_node(self, data):
		current_node = self.head

		if current_node.data == data:
			self.remove_first_node()
			return

		while(current_node != None and current_node.next.data != data):
			current_node = current_node.next

		if current_node == None:
			return
		else:
			current_node.next = current_node.next.next

# sizeOfLL აბრუნებს linked list-ის ზომას(node-ების რაოდენობას.) საწყისი რიცხვი ნოლია, და ყოველ node-ზე ერთით იზრდება.თუ სია ცარიელია, აბრუნებს 0-ს. 

	def sizeOfLL(self):
		size = 0
		if(self.head):
			current_node = self.head
			while(current_node):
				size = size+1
				current_node = current_node.next
			return size
		else:
			return 0

# ბეჭდავს linked list-ში არსებული თითოეული node-ის მონაცემებს.(იწყებს head-იდან და სიას გაივლის სათითაოდ.)

	def printLL(self):
		current_node = self.head
		while(current_node):
			print(current_node.data)
			current_node = current_node.next

# გამოყენების მაგალითები:

llist = LinkedList()

llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

print("Node Data")
llist.printLL()

print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)


print("\nLinked list after removing a node:")
llist.printLL()

print("\nUpdate node Value")
llist.updateNode('z', 0)
llist.printLL()

print("\nSize of linked list :", end=" ")
print(llist.sizeOfLL())