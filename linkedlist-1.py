# 1-->2-->3-->7-->5-->6-->none
# index=4
#class used to create a single node for the linkedlist
class Node:
    def __init__(self,data):
        self.data=data
        self.ptr=None
# class to create a linkedlist by using nodes from Node class
class LinkedList:
    def __init__(self):
        self.head=None
    # add an item from the first or head
    def fromstart(self,data):
        #creating a new node with the help of Node class by giving 'data' as input data.
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        else:
            newnode.ptr=self.head
            self.head=newnode
    # add an item at the end of list
    def fromend(self,data):
        newnode=Node(data)
        current=self.head
        while current.ptr:
            current=current.ptr 
        current.ptr=newnode
    # add an item at a specified index
    def atindex(self,data,index):
        current=self.head
        newnode=Node(data)
        position=0
        while(current!=None and position+1!=index):
            current=current.ptr
            position=position+1
        newnode.ptr=current.ptr
        current.ptr=newnode
    # update an item at a specified index
    def update(self,val,index):
        current=self.head
        position=0
        if position==index:
            current.data=val
        while(current!=None and position+1!=index):
            current=current.ptr
            position+=1
        current=current.ptr
        current.data=val
    #delete at the first index
    def delstart(self):
        if self.head==None:
            return
        self.head=self.head.ptr
    #deleting an item at specified Index
    def delatindex(self,index):
        
        position=0
        if position==index:
            self.head=self.head.ptr
        current=self.head
        while current!=None and position+1!=index:
            current=current.ptr
            position+=1
        current.ptr=current.ptr.ptr
     # for printing the required functions   
    def printll(self):
        current=self.head
        while(current):
            print(current.data,end='-->')
            current=current.ptr
ll=LinkedList()
ll.fromstart(1)
ll.fromstart(2)
ll.fromstart(3)
ll.fromstart(4)
ll.fromend(5)
ll.atindex(7,4)
ll.update(10,3)
ll.delstart()
ll.delatindex(3)
ll.printll()