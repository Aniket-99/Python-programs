class Node(object):

    def __init__(self,value):
        self.info = value
        self.prev = None
        self.next = None


class DoubleLinkedList(object):

    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("Double Linked List is empty")
            return

        print("List is: ")
        p = self.start

        while p is not None:
            print(p.info ," ",end='')
            p = p.next
        print()


    def insert_in_beginning(self,data):
        temp = Node(data)
        temp.next = self.start
        self.start.prev = temp
        self.start = temp

    def insert_in_empty_list(self,data):
        temp = Node(data)
        self.start = temp

    def insert_at_end(self,data):
        temp = Node(data)
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p

    def create_list(self):
        n = int(input("Enter the number of Nodes: "))
        if n == 0:
            return
        data = int(input("Enter the first element to be inserted: "))
        self.insert_in_empty_list(data)

        for i in range(n-1):
            data = int(input("Enter the next element to be inserted: "))
            self.insert_at_end(data)

    def insert_after(self,data,x):
        temp = Node(data)
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next

        if p is None:
            print(x," is not present in the list")
        else:
            temp.prev = p
            temp.next = p.next
            if p.next is not None:
                p.next.prev = temp
            p.next = temp
        
    def insert_before(self,data,x):
        if self.start is None:
            print("List is empty")
            return

        if self.start.info == x:
            temp = Node(data)
            temp.next = self.start
            self.start.prev = temp
            self.start = temp
            return

        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next


        if p is None:
            print(x,"is not present in tne list")
        else:
            temp = Node(data)
            temp.prev = p.prev
            temp.next = p
            p.prev.next = temp
            p.prev = temp

    def delete_first_node(self):
        if self.start is None:
            print("List is empty")

        if self.start.next is None:
            self.start = None
            return
        self.start = self.start.next
        self.start.prev = None

    def delete_last_node(self):
        if self.start is None:
            print("list is empty")
            return
        if self.start.next is None:
            self.start = None
            return
        p = self.start
        while p.next is not None:
            p = p.next
        p.prev.next = None


    def delete_node(self,x):
        if self.start is None:
            return
        if self.start.next is None:
            if self.start.info == x:
                self.start = None
            else:
                print(x," not found")
            return
        
        #deletion of first node
        if self.start.info == x:
            self.start = self.start.next
            self.start.prev = None
            return

        p = self.start
        while p.next is not None:
            if p.info == x:
                break
            p = p.next

        if p.next is not None: #Node to be deleted is in between
            p.prev.next = p.next
            p.next.prev = p.prev
        else: #p refers to last node
            if p.info == x:
                p.prev.next = None
            else:
                print(x," not found")
            
            
    def reverse_list(self):
        if self.start is None:
            return

        p1 = self.start
        p2 = p1.next
        p1.next = None
        p1.prev = p2
        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev
        self.start = p1
            

    
list = DoubleLinkedList()
list.create_list() 
while True:
    print("1.Display the list")
    print("2.Insert a node at the beginning")
    print("3.Insert in empty list")
    print("4.Insert at end of list")
    print("5.insert after an element")
    print("6.Insert after an elemet")
    print("7.Delete first node")
    print("8.delete last node")
    print("9.delete any node")
    print("10.Reverse the list")
    option = int(input("Enter your option: "))

    if option == 1:
        list.display_list()
    elif option == 2:
        data = int(input("enter the element to be inserted: "))
        list.insert_in_beginning(data)
    elif option == 3:
        data = int(input("enter the element to be inserted: "))
        list.insert_in_empty_list(data)
    elif option == 4:
        data = int(input("enter the element to be inserted: "))
        list.insert_at_end(data)
    elif option == 5:
        x = int(input("Enter the element after which the element is to be inserted"))
        data = int(input("enter the element to be inserted: "))
        list.insert_after(data,x)
    elif option == 6:
        x = int(input("Enter the element before which the element is to be inserted"))
        data = int(input("enter the element to be inserted: "))
        list.insert_before(data,x)
    elif option == 7:
        list.delete_first_node()
    elif option == 8:
        list.delete_last_node()
    elif option == 9:
        x = int(input("Enter the element to be deleted"))
        list.delete_node(x)
    elif option == 10:
        list.reverse_list()
    else:
        break
