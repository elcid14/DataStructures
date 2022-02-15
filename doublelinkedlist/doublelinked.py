#This is a basic implementation of a double linked list
#A double linked list is a list that has previous value and next value. 


class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None




class DoubleList:

    def __init__(self):
        self.head = None



    #define method to insert into 
    def insertNode(self, data):
        if self.head is None :
            print("Inserting into double linked list with no head")
            newHead = Node(data)
            self.head = newHead
            return
        elif self.head is not None:
            print("Inserting node into list with head")
            head = self.head
            newNode = Node(data)
            while head.next is not None:
                head = head.next
            head.next = newNode
            newNode.prev = head
        else:
            print("Inserting new node")
            newNode = Node(data)
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = None


    def printNodes(self):
        if(self.head == None):
            print("No starting Node") 
        list = self.head
        while(list):
            print(list.data)
            list = list.next


if __name__ == '__main__':
    nodeOne = Node(1)
    dList = DoubleList()
    dList.insertNode(nodeOne.data)
    dList.printNodes()
    dList.insertNode(2)
    dList.insertNode(3)
    dList.printNodes()
