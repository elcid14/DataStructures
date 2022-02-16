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

    #pop head from double linked list
    #if there is self.head and 

    def popHead(self):
        if self.head is None:
            print("No head in list")
            return
        elif self.head.next is not None:
            self.head = self.head.next
            self.head.prev = None

    #slice last node from the double linked list
    def slice(self):
        if self.head is None:
            print("Empty list")
            return
        elif self.head.next is not None:
            print("Slicing last node from double linked list")
            head = self.head
            while head.next is not None:
                head = head.next
            head.prev.next = None
        else:
            print("Slicing head from list")
            if self.head.next is None:
                self.head = None
                return
    #delete any nth node from the double linked list
    def removeNode(self, node):
       temp = self.head
       #define bail out if none
       if temp is None or node is None:
           return
        #delete if node is head
       elif temp.data == node:
           print("Deleting node that is head of list")
           self.head = temp.next
           self.head.prev = None
        #delete if last node
       elif temp.data == node and temp.next is None:
           print(temp.prev.next)
           #temp.next.prev = temp.prev   
       else:
           while temp:
               if temp.data == node:
                   temp.prev.next = temp.next
                   temp.next.prev = temp.prev
               temp = temp.next

    def getLastNode(self):
        head = self.head
        if self.head.next is not None:
            while head.next is not None:
                head = head.next
            print(head.prev.next.data)
            



        
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
    print("INSERT NODES-----------------")
    dList.insertNode(2)
    dList.insertNode(3)
    dList.printNodes()
    print("DELETE HEAD--------------")
    dList.popHead()
    dList.printNodes()
    print("DELETE HEAD--------------")
    dList.popHead()
    dList.printNodes()
    print("DELETE LAST NODE IN LIST----------")
    dList.insertNode(1)
    dList.insertNode(2)
    dList.printNodes()
    print("--------------------")
    dList.slice()
    dList.printNodes()
    dList.insertNode(1)
    dList.insertNode(2)
    dList.insertNode("Test")
    dList.insertNode("Test TWO")
    dList.insertNode(5)
    print("--------------------")
    dList.printNodes()
    print("REMOVING NODE FROM LIST AT ANY POS---------------------")
    dList.getLastNode()
    #dList.printNodes()
    