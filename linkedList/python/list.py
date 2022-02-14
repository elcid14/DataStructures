#Python version of linked list. This is singly linked list


#define Node class. Object used to store the actual data
class Node:
    
    def __init__(self,data):
        self.data = data #stores data of node object
        self.next = None #stores next node for List class. None by default



#defines List class. 

class List:

    def __init__(self):
        self.head = None #stores head of the list. Is None by default

    #Inserts new node into list. Make new node the new head and existiing head the next of new node
    def pushNode(self, newData):
        if(self.head == None):
            print("Linked list does not have head")
            newHead = Node(newData)
            self.head = newHead
            newHead.next = None
        else:
            print("Inserting New Node")
            newNode = Node(newData)
            newNode.next = self.head
            self.head = newNode

#adds node to tail
    def pushNodeToTail(self, newData):
        newTail = Node(newData)
        temp = self.head
        if(self.head == None):
            self.head = newTail
            self.head.next = None
            return
        while(temp.next != None):
            temp = temp.next
        temp.next = newTail
        

    #removes node from any part of the linked list
    def removeNode(self, node):
        temp = self.head



    #removes head from the list
    def removeHeadFromList(self):
        temp = self.head
        if(temp is not None):
            self.head = temp.next
            temp = None
            return

    #removes tail from list
    def removeTail(self):
       if(self.head != None):
           temp = self.head
           while(temp.next.next != None):
               temp = temp.next
           endNode = temp.next
           temp.next = None
           endNode = None
       elif(self.head is None):
           print("No head in list")
       elif(self.head.next is None):
           self.head = None


    #prints out all nodes in list. Simple while loop to itereate through list starting at head and call next if present

    def printNodes(self):
        if(self.head == None):
            print("No starting Node") 
        list = self.head
        while(list):
            print(list.data)
            list = list.next


if __name__ =='__main__':
    #create nodes
    nodeOne = Node({"message":"Head of List"})
    nodeTwo = Node({"message":"Node Two"})
    nodeThree = Node({"message":"Node Three"})
    nodeFour = Node({"message":"Node Four/ Tail"})

    #create linked list

    list = List()

    list.head = nodeOne
    nodeOne.next = nodeTwo
    nodeTwo.next = nodeThree
    nodeThree.next = nodeFour

    #list.printNodes()

    #test push method
    print("PUSHING NODE TO HEAD---------------")
    newNodeTest = Node({"message":"New Node"})
    list.pushNode({"message":"New Node"})
    list.printNodes()


    # test delete nodes
    print("REMOVING TAIL-----------------")
    list.removeTail()
    list.printNodes()
    listTwo = List()
    listTwo.removeTail()


    #test adding node as new tail
    print("ADDING NEW NODE AS TAIL---------------")
    list.pushNodeToTail({"message":"NEW Tail"})
    list.printNodes()
    print("ADDING NEW NODE AS TAIL TO LIST WITH NO HEAD---------------")
    listTwo.pushNodeToTail({"message":"NEW Tail to list with no head"})
    listTwo.printNodes()


    #removes head from a list
    print("REMOVING HEAD FROM LIST---------------")
    list.removeHeadFromList()
    list.printNodes()

    #push node to empty list
    print("PUSHING NODE TO HEAD OF EMPTY LIST---------------")
    listThree = List()
    listThree.pushNode({"message":"Head, First Node"})
    listThree.printNodes()