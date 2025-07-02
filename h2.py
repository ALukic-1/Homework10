class Node ():
    def __init__ (self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def add (self, value):
        if value > self.value:
            if self.right is None:
                self.right = Node (value)
            else:
                self.right.add(value)
        else:
            if self.left is None:
                self.left = Node (value)
            else:
                self.left.add(value)

    def get_value(self, value):
        if value is self.value:
            return self
        elif value < self.value and self.left:
           return self.left.get_value(value)
        elif value > self.value and self.right:
            return self.right.get_value(value)
        else:
            return None


    def remove(self, value, parent=None):
        if value < self.value:
            if self.left:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right:
                self.right.remove(value, self)
        else:
            if self.left and self.right:
                successor = self.right._find_min()
                self.value = successor.value
                self.right.remove(successor.value, self)
            elif parent:
                if parent.left == self:
                    parent.left = self.left if self.left else self.right
                elif parent.right == self:
                    parent.right = self.left if self.left else self.rightv

    def print(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + str(self.value))
        if self.left:
            self.left.print(level + 1, prefix="L--- ")
        if self.right:
            self.right.print(level + 1, prefix="R--- ")


class BinaryTree:
    def __init__ (self):
        self.root = None

    def add (self, value):
        if self.root is None:
            self.root = Node (value)
        else:
            self.root.add(value)


    def get(self,value):
        if self.root:
            return self.root.get(value)
        return None

    def remove(self,value):
        if self.root:
            if self.root.value == value:
                # Special case: removing the root node
                temp = Node(0)
                temp.left = self.root
                self.root.remove(value, temp)
                self.root = temp.left
            else:
                self.root.remove(value)

    def print(self):
        if self.root is None:
            print("Empty tree")
        else:
            self.root.print()



class H2main ():
    bt = BinaryTree()
    bt.add(10)
    bt.add(6)
    bt.add(20)
    bt.add(4)
    bt.add(8)
    bt.add(30)
    bt.add(5)
    bt.add(7)
    bt.print()