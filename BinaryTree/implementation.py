'''
Step 1 - I really focused and improved upon how I START thinking about the question. This is the most important step according to me. You may know all the data structures in the world, but if you dont start off correctly with a problem, you cant do much. So first step is to just think about how you will start!
In my case I started of by writing all the inputs given to me, all the outputs required and constraints if any
Step 2 - What next? Well now think which data structure will solve the problem?
Step 3 - Is there something you should do before using the data structure? Like sorting, arranging, or anything that makes the it easy for the data structure to solve that problem. More often than not, sorting a given input can do wonders
Step 4 - Write down all the steps you will be performing. Don’t even think about writing code right now. Just write the steps and write the expected Big O complexity and space complexity
Step 5 - Now optimize the solution you wrote above. Were you at least able to write a brute force? Can you use another data structure to improve the complexities ? Can you pre-process the input to reduce the complexities?
Step 6 - Only when you are absolutely sure about the optimal solution, start writing the code.
'''
class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():

    def __init__(self, value):
        self.root = Node(value)


    def print_tree(self, traversal_type):
        if(traversal_type == "preorder"):
            return print(self.preorder_print(self.root, ""))
        elif (traversal_type == "inorder"):
            return print(self.inorder_print(self.root, ""))
        elif (traversal_type == "postorder"):
            return print(self.postorder_print(self.root, ""))
        else:
            print("Traversal type not supported.")

    def preorder_print(self, start, traversal):
        #Root -> Left -> Rigth
        if start:
            traversal += (str(start.value) + " - ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        #Left -> Root -> Right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + " - ")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        #Left -> Right -> Root
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + " - ")

        return traversal




tree = BinaryTree(1)

#           1
#          /  \
#         /    \
#        2      3
#       / \    / \
#      4   5   6  7
#                  \
#                   8

tree.root.left = Node(2)

#          1
#         /
#        2

tree.root.right = Node(3)

#          1
#         / \
#        2   3

tree.root.left.left = Node(4)

#          1
#         / \
#        2   3
#       /
#      4

tree.root.left.right = Node(5)
#          1
#         / \
#        2   3
#       / \
#      4   5

tree.root.right.left = Node(6)
#           1
#          /  \
#         /    \
#        2      3
#       / \    /
#      4   5   6

tree.root.right.right = Node(7)

#           1
#          /  \
#         /    \
#        2      3
#       / \    / \
#      4   5   6  7
tree.root.right.right.right = Node(8)

#           1
#          /  \
#         /    \
#        2      3
#       / \    / \
#      4   5   6  7
#                  \
#                   8

mystring = tree.print_tree("preorder")

mystring = tree.print_tree("inorder")
mystring = tree.print_tree("postorder")





