# author: Jacob Shearer
# date: 5/5/2023
# file: tree.py contains an implementation of a BinaryTree as well as a child class meant for storing
# mathemetical expressions.
# input: strings
# output: floating point numbers

from stack import Stack


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        left = '()' if self.leftChild is None else f'({self.leftChild})'
        right = '()' if self.rightChild is None else f'({self.rightChild})'
        return f'{self.key}{left}{right}'

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        if self.leftChild is None:
            return None
        else:
            return self.leftChild

    def getRightChild(self):
        if self.rightChild is None:
            return None
        else:
            return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


class ExpTree(BinaryTree):
    def __str__(self):
        return ExpTree.inorder(self)

    @staticmethod
    def make_tree(postfix):
        tree_stack = Stack()
        for char in postfix:
            temp_tree = ExpTree(char)
            # Operands are made the root node of their own trees
            if char.isdigit() or char.replace('.', '').isdigit():
                tree_stack.push(temp_tree)
            # Operators are also made the root node of their own trees but with children taken from the tree stack
            else:
                temp_tree.rightChild = tree_stack.pop()
                temp_tree.leftChild = tree_stack.pop()
                tree_stack.push(temp_tree)

        return tree_stack.pop()

    # Traverses the tree in root->left->right and returns the resulting traversal string
    @staticmethod
    def preorder(tree):
        if tree.leftChild is None and tree.rightChild is None:
            return tree.key
        else:
            left = ExpTree.preorder(tree.leftChild)
            right = ExpTree.preorder(tree.rightChild)
            return f'{tree.key}{left}{right}'

    # Traverses the tree in left->right->root and returns the resulting traversal string
    @staticmethod
    def postorder(tree):
        if tree.leftChild is None and tree.rightChild is None:
            return tree.key
        else:
            left = ExpTree.postorder(tree.leftChild)
            right = ExpTree.postorder(tree.rightChild)
            return f'{left}{right}{tree.key}'

    # Traverses the tree in left->root->right and returns the resulting traversal string (with parentheses)
    @staticmethod
    def inorder(tree):
        if tree.leftChild is None and tree.rightChild is None:
            return tree.key
        else:
            left = ExpTree.inorder(tree.leftChild)
            right = ExpTree.inorder(tree.rightChild)
            return f'({left}{tree.key}{right})'

    # Returns the value of the whole tree by evaluating the expressions stored in each subtree
    @staticmethod
    def evaluate(tree):
        operators = {'+': lambda x, y: x+y, '-': lambda x, y: x - y,
                     '*': lambda x, y: x*y, '/': lambda x, y: x/y,
                     '^': lambda x, y: x**y}

        # Operand only subtrees simply return their value
        if tree.leftChild is None and tree.rightChild is None:
            return float(tree.key)
        # Complete subtrees (which contain expressions) are evaluated and return their value
        else:
            left = ExpTree.evaluate(tree.leftChild)
            right = ExpTree.evaluate(tree.rightChild)
            return operators[tree.key](left, right)


# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    # test a BinaryTree
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild() is None
    assert r.getRightChild() is None
    assert str(r) == 'a()()'

    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'

    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'

    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    # test an ExpTree
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
