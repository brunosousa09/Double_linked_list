from time import sleep 

class DoubleNode:
    
    def __init__(self, data):
       self.data=data
       self.next=None
       self.later=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.end=None

    def append(self, data):
        
        new_node = DoubleNode(data)    
        new_node.next = None

        if self.head==None:
            new_node.later = None
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            
            last_node = last_node.next
        
        last_node.next = new_node
        new_node.later = last_node
        return 

    def length(self):
        if self.head == None:
            return 0
        momentary = self.head
        total = 0

        while momentary:
            total+=1
            momentary=momentary.next
        return total

    def the_list(self):
         node_data = []
         momentary = self.head

         while momentary:
            node_data.append(momentary.data)
            momentary = momentary.next
         return node_data


    def reverse(self):
        if self.head is None:
            print('The list has no elements to reverse')
            return 0
        momentary = self.head
        new_node = momentary.next
        momentary.next = None
        momentary.later = new_node
        while new_node != None:
            new_node.later = new_node.next
            new_node.next = momentary
            momentary = new_node
            new_node = new_node.later
        self.head = momentary

    def display(self):
        object = self.head
        if object is None:
            print('List has no elements')
        while object:
            print(object.data)
            object=object.next
        print('---------------')

    def insert_at_start(self, data):
        if self.head == None:
            new_node = DoubleNode(data)
            self.head = new_node
            print('Node inserted')
            return
        new_node = DoubleNode(data)
        new_node.next = self.head
        self.head.later = new_node
        self.head = new_node 

    def insert_at_end(self, data):
        if self.head == None:
            new_node = DoubleNode(data)
            self.head = new_node
            return
        momentary = self.head
        while momentary.next != None:
            momentary = momentary.next
        new_node = DoubleNode(data)
        momentary.next = new_node
        new_node.later = momentary

    def delete_element_by_start(self):
        if self.head == None:
            print('The list has no element to delete')
            return
        if self.head.next == None:
            self.head = None
            return
        self.head = self.head.next
        self.start_prev = None        

    def delete_element_by_end(self):
        if self.head == None:
            print('The list has no element to delete')        
            return
        if self.head.next == None:
            self.head = None
            return
        momentary = self.head
        while momentary.next != None:
            momentary = momentary.next
        momentary.later.next = None

    def delete_element_by_value(self, value):        
        if self.head == None:
            print('The list has no element to delete')
            return
        if self.head.next == None:
            if self.head.item == value:
                self.head = None
            else:
                print('Item not found')
            return            
        if self.head.data == value:
            self.head = self.head.next
            self.head.later = None
            return

        momentary = self.head
        while momentary.next != None:
            if momentary.data == value:
                break
            momentary = momentary.next
        if momentary.next != None:
            momentary.later.next = momentary.next
            momentary.next.later = momentary.later
        else:
            if momentary.data == value:
                momentary.later.next = None
            else:
                print('Element not found') 


myList=DoubleLinkedList()
myList.display()

myList.append(3)
myList.append(4)
myList.append(5)
myList.append(6)
myList.append(7)
myList.append(8)

myList.display()

sleep(1)

print('The total number of elements are: ' + str(myList.length()))
print(myList.the_list())
print('~~~~~~~~~~~~~~~~')

sleep(1)

myList.reverse()
myList.display()

sleep(1)

myList.delete_element_by_start()
myList.display()

sleep(1)

myList.delete_element_by_end()
myList.display()

sleep(1)

myList.insert_at_start(1)
myList.display()

sleep(1)

myList.insert_at_end(3)
myList.display()

sleep(1)

myList.delete_element_by_value(7)
myList.display()

sleep(1)

