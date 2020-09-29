# -*- coding: utf-8 -*-
class Stack:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

    def __str__(self):
        stackString = "["
        for i in self.items:
            stackString += ", " + str(i)
        stackString += "]"
        return stackString

"""
s = Stack()

print(s.isEmpty())

s.push(4)
s.push('Dog')
print(s.peek())

s.push(True)

print(s.size())

print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
"""