class User:
    # users = [] * 100
    def __init__(self, username=None, name=None, email=None):
        self.username = username
        self.name = name
        self.email = email

        # User.users.append(self)
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()



class UserDatabase:
    users = []
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users


class TreeNode:
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

    def height(self):
        """The height/depth of a binary tree is defined
        as the length of the longest path from its root
        node to a leaf."""
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        """Here's a function to count the number
        of nodes in a binary tree."""
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        """Here's an implementation of inorder
        traversal of a binary tree."""
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left) +
                [self.key] +
                TreeNode.traverse_in_order(self.right))

    def display_keys(self, space='\t', level=0):
        """helper function to display all the keys in a
        tree-like structure for easier visualization"""
        # If the node is empty
        if self is None:
            print(space * level + '∅')
            return
            # If the node is a leaf
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return
        # If the node has children
        if self.right is not None:
            self.right.display_keys(space, level + 1)
        print(space * level + str(self.key))
        if self.left is not None:
            self.left.display_keys(space, level + 1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    # @staticmethod
    def remove_none(nums):
        return [x for x in nums if x is not None]

    # @staticmethod
    def is_bst(node):
        if node is None:
            return True, None, None

        is_bst_l, min_l, max_l = TreeNode.is_bst(node.left)
        is_bst_r, min_r, max_r = TreeNode.is_bst(node.right)

        is_bst_node = (is_bst_l and is_bst_r and
                       (max_l is None or node.key > max_l) and
                       (min_r is None or node.key < min_r))

        min_key = min(TreeNode.remove_none([min_l, node.key, min_r]))
        max_key = max(TreeNode.remove_none([max_l, node.key, max_r]))

        # print(node.key, min_key, max_key, is_bst_node)

        return is_bst_node, min_key, max_key

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def display_keys(self, space='\t', level=0):
        if self is None:
            print(space * level + '∅')
            return

        if self.right is not None:
            self.right.display_keys(space, level + 1)

        print(space * level + str(self.key))

        if self.left is not None:
            self.left.display_keys(space, level + 1)

    def insert(self, key, value):
        if key < self.key:
            if self.left is None:
                self.left = BSTNode(key, value)
                self.left.parent = self
            else:
                self.left.insert(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = BSTNode(key, value)
                self.right.parent = self
            else:
                self.right.insert(key, value)

    def find(self, key):
        if self is None:
            return None
        if key == self.key:
            return self
        if key < self.key:
            return self.left.find(key) if self.left else None
        if key > self.key:
            return self.right.find(key) if self.right else None

    def list_all(self):
        if self is None:
            return []
        return BSTNode.list_all(self.left) + [(self.key, self.value)] + BSTNode.list_all(self.right)


node = TreeNode(2)
node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(7)
node6 = TreeNode(4)
node7 = TreeNode(6)
node8 = TreeNode(8)

node.left = node1
node.right = node2
node1.left = node3
node2.left = node4
node2.right = node5
node4.right = node6
node5.left = node7
node5.right = node8

# print(node.right.left.right.key, node.right.right.left.key, node.right.right.right.key)


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

# users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]
database = UserDatabase()

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)
database.insert(biraj)

database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))

user = database.list_all()


tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
# tree = TreeNode.parse_tuple(tree_tuple)
# tree.display_keys('  ')
tree1 = TreeNode.parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))

tree2 = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth'), 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
is_bst, minkey, maxkey = TreeNode.is_bst(tree2)
# print("Is BST:", is_bst, minkey, maxkey)

tree = BSTNode(jadhesh.username, jadhesh)
# tree.left = BSTNode(biraj.username, biraj)
# tree.right = BSTNode(sonaksh.username, sonaksh)
# tree.left.left = BSTNode(aakash.username, aakash)
# tree.left.right = BSTNode(hemanth.username, hemanth)
# tree.right.left = BSTNode(siddhant.username, siddhant)
# tree.right.right = BSTNode(vishal.username, vishal)

tree.insert(biraj.username, biraj)
tree.insert(sonaksh.username, sonaksh)
tree.insert(aakash.username, aakash)
tree.insert(hemanth.username, hemanth)
tree.insert(siddhant.username, siddhant)
tree.insert(vishal.username, siddhant)

tree2 = BSTNode(aakash.username, aakash)
tree2.insert(biraj.username, biraj)
tree2.insert(hemanth.username, hemanth)
tree2.insert(jadhesh.username, jadhesh)
tree2.insert(siddhant.username, siddhant)
tree2.insert(sonaksh.username, sonaksh)
tree2.insert(vishal.username, vishal)

# tree2.display_keys("  ")
node = BSTNode.list_all(tree)

print(node)
