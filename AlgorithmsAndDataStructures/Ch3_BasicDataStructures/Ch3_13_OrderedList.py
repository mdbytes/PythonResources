from Ch3_BasicDataStructures.Ch3_11_Node import Node

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,data):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > data:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(data)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self, data):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == data:
                found = True
            else:
                if current.getData() > data:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def remove(self,data):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

mylist = OrderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)


print(mylist.length())
print(mylist.search(31))
print(mylist.search(99))
print(mylist.search(77))
mylist.remove(77)
print(mylist.search(77))