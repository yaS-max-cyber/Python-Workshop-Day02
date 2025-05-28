class Node:
    
    def __init__(self,data):
        self.data = data 
        self.next = None
    
#LInked list class contain a node object   
class LinkedList:
    #function to initialise head 
    def __init__(self):
        self.head= None

    def listprint(self):
        printval = self.head

        while printval is not None:
            print(printval.data)
            printval = printval.next

    def _inset_at_Begining(self,newdata):
        newdata = Node(newdata)
        newdata.next = self.head
        self.head = newdata

l1 =LinkedList()      
l1.head =Node("Toyota")  
l2 = Node("BMW")
l3 = Node("Audi")
l4 = Node("Lambogini")
l1.head.next = l2
l2.next = l3
l3.next = l4
l1.listprint()
print("")
l1._inset_at_Begining("Benz")
l1.listprint()