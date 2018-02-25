class Dictionary:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        node = self.search(self.root, key)
        if node is not None:
            return node.value
        raise KeyError

    def __setitem__(self, key, value):
        if self.root:
            self.put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size = self.size + 1

    def put(self, key, value, currentNode):
        if key < currentNode.key:
            if currentNode.left is not None:
                self.put(key, value, currentNode.left)
            else:
                currentNode.left = TreeNode(key, value, parent=currentNode)
        elif key > currentNode.key:
            if currentNode.right is not None:
                self.put(key, value, currentNode.right)
            else:
                currentNode.right = TreeNode(key, value, parent=currentNode)
        else:
            currentNode.value = value
            self.size -= 1

    def __delitem__(self, key):
        if self.size > 1:
            node = self.search(self.root, key)
            if node is not None:
                self.delete(node)
                self.size -= 1
            else:
                raise KeyError
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError

    def delete(self, node):
        if node.left is None and node.right is None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        elif (node.left is None and node.right is not None) or (
                        node.left is not None and node.right is None):
            if node.left is not None:
                if node.parent.left == node:
                    node.left.parent = node.parent
                    node.parent.left = node.left
                elif node.parent.right == node:
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:
                    node.value = node.left.value
                    node.key = node.left.key
                    node.left = node.left.left
                    node.right = node.left.right
                    node.parent = None
            else:
                if node.parent.left == node:
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.parent.right == node:
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    node.value = node.right.value
                    node.key = node.right.key
                    node.left = node.right.left
                    node.right = node.right.right
                    node.parent = None
        else:
            alternative = node.find_alternative()
            alternative.splice()
            node.key = alternative.key
            node.value = alternative.value

    def find_alternative(self):
        if self.right is not None:
            alt = self.right.get_min_value()
        else:
            if self.parent:
                if self.parent.left == self:
                    alt = self.parent
                else:
                    self.parent.right = None
                    alt = self.parent.find_alternative()
                    self.parent.right = self
        return alt

    def get_min_value(self):
        cur = self
        while cur.left is not None:
            cur = cur.left
        return cur

    def splice(self):
        if self.right is not None or self.left is not None:
            if self.left is not None:
                if self.parent.left == self:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.parent.left == self:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent
        elif self.right is None and self.left is None:
            if self.parent.left == self:
                self.parent.left = None
            else:
                self.parent.right = None

    def search(self, root, element):
        if root is None:
            return None
        elif element == root.key:
            return root
        elif element < root.key:
            return self.search(root.left, element)
        else:
            return self.search(root.right, element)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.value = val
        self.left = left
        self.right = right
        self.parent = parent


def main():
    a = Dictionary()
    a[1] = 'Ok'
    a[2] = 'q'
    a[1] = 0
    a[7] = 'p'
    a[10] = 1
    a[0] = 5
    a[3] = 2
    print(a.size)
    print(a[7])
    print(a[2])
    print(a[3])
    print(a[0])
    print(a[10])
    print(a.size)
    print(a[7])
    print(a[2])
    print(a[3])
    print(a[0])
    print(a[10])
    a.__delitem__(0)
    print(a[0])


if __name__ == '__main__':
    main()
