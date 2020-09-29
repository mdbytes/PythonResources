from Ch3_BasicDataStructures.Ch3_01_Stack import Stack
from Ch6_Trees.Ch6_01_BinaryTree import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insterLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i not in '+-*/)':
            currentTree.setRootValue(eval(i))
            parent = pStack.pop()
            currentTree = parent

        elif i in '+-*/':
            currentTree.setRootValue(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        else:
            raise ValueError("Unknown Operator: " + i)

    return eTree






