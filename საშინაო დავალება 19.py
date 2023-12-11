# 1.მოიძიე და გაარჩიე ხის მონაცემთა სტრუქტურის კოდის მაგალითი.

# შექმნილია კლასი Node, რომლის შიგნითაც გვაქვს init ფუნქცია, (კონსტრუქტორი). value არის პარამეტრი, რომელშიც მონაცემები შეინახება.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# შემდეგ შექმნილია კლასი BinaryTree, რომელსაც ასევე აქვს init კონსტრუქტორი. მას აქვს root პარამეტრი, რაც არის საწყისი მნიშვნელობა. 

class BinaryTree:
    def __init__(self, root):
        # შემდეგ ეს ფუნქცია ქმნის node ობიექტს, რომელსაც მნიშვნელობად ექნება root მნიშვნელობა

        self.root = Node(root)
#  insert მეთოდით შეგვიძლია ამ"ხეში" ახალი მნიშვნელობა შევინახოთ

    def insert(self, value):
        self._insert(self.root, value)

# შემდეგი არის რეკურსიული ფუნქცია, რომ შევინახოთ ინფორმაცია. ის იღებს ამჟამინდელ node-ს და იმ მნიშვნელობას, რომელიც უნდა ჩაწეროს. 
    def _insert(self, current_node, value):
        # ამოწმებს ახალი მნიშვნელობა ნაკლებია თუ არა ამჟამინდელ node-ზე.
        if value < current_node.value:
            # თუ მნიშვნელობა არის ამჟამინდელი node-ის მნიშვნელობაზე ნაკლები ახალი node იქმნება ახალი მნიშვნელობით.
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            # თუ მნიშვნელობა მეტია ამჟამინდელი node-ის მნიშვნელობაზე, იქმნება ახალი node. 
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)
        # ხოლო თუ მნიშვნელობა არც დიდია და არც პატარა node-ზე, გამოიტანს შეტყობინებას - 'Value already exists in the tree'
        else:
            print(f"Value {value} already exists in the tree.")

# ეს ფუქნცია ბეჭდავს ხის ელემენტებს. 
    def print_tree(self):
        # ამოწმებს ხეს აქვს თუ არა root.
        if self.root:
            self._print_tree(self.root)
# ეს არის რეკურსიული დამხმარე ფუნქცია, რომ დაბეჭდოს ხის ელემენტები.

    def _print_tree(self, current_node):
        # ამოწმებს ამჟამინდელი Node ხომ არ არის none
        if current_node:
            self._print_tree(current_node.left)
            print(current_node.value, end=' ')
            self._print_tree(current_node.right)

# გამოყენების მაგალითები
tree = BinaryTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(20)

print("Binary Search Tree:")
tree.print_tree()
