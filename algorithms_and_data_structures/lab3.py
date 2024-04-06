from tkinter import *

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        #self.tail = None
        #self.current = None
    def empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if self.empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def print_list(self):
        current = self.head
        text = ""
        while current:
            #print(current.data)
            text += str(current.data) + " "
            current = current.next
        return text

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return False

    def remove(self, data):
        current = self.search(data)
        if current == False:
            print ("no such element")
        else:
            if current.prev:
                current.prev.next = current.next
            else:
                self.head = current.next
            if current.next:
                current.next.prev = current.prev
            return



llist = DoublyLinkedList()
llist.append(1)
llist.append(2)
llist.append(3)

wind = Tk()
wind.title("lab3")
wind.geometry('350x200')

#lbl = Label(wind, text = "enter text"); lbl.grid()

#entry = Entry(wind, width=57); entry.grid(column = 0, row = 1)

lbl2 = Label(wind, text="enter key")
lbl2.grid(column=0, row=2)

enter2 = Entry(wind, width=20)
enter2.grid(column=0, row=3)

def app():
    llist.append(int(enter2.get()))

def prep():
    llist.prepend(int(enter2.get()))

def rm():
    llist.remove(int(enter2.get()))

def update():
    lbl3.configure(text=llist.print_list())

btn = Button(wind, text = "remove", fg = "red", command=rm)
btn.grid(column=0, row=4)

btn2 = Button(wind, text = "append", fg = "red", command=app)
btn2.grid(column=0, row=5)

btn3 = Button(wind, text = "prepend", fg = "red", command=prep)
btn3.grid(column=0, row=6)

btn3 = Button(wind, text = "update", fg = "red", command=update)
btn3.grid(column=0, row=7)

lbl3 = Label(wind, text=llist.print_list())
lbl3.grid(column=0, row=8)


wind.mainloop()
