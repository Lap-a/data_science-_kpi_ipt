from tkinter import *

class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def empty(self):
        return self.head is None

    def search(self, key):
        current = self.head
        result = []
        while current:
            if current.key == key:
                result.append(current)
            current = current.next
        return result

    def append(self, key):# at the end
        new_node = Node(key)
        if self.empty():
            self.head = self.tail = self.current = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, key):# at the start
        new_node = Node(key)
        if self.empty():
            self.head = self.tail = self.current = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    def insert_after(self, key, new_key):
        currents = self.search(key)
        if len(currents) == 0:
            print ("no such element")
        else:
            for current in currents:
                if current.next:
                    new_node = Node(new_key)
                    new_node.prev = current
                    new_node.next = current.next
                    current.next.prev = new_node
                    current.next = new_node
                else:
                    self.append(new_key)

    def print_list(self):
        current = self.head
        text = ""
        while current:
            text += str(current.key) + " "
            current = current.next
        return text

    def remove(self, key): #obj not deleted. u just cannot see it
        currents = self.search(key)
        if len(currents) == 0:
            print ("no such element")
        else:
            for current in currents:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev

    
    def lab_function(self):
        for i in range(10):
            self.remove(str(i))
        self.insert_after("a", "a")

        current = self.tail
        while current: # find last space
            if current.key == " ":
                self.tail = current.prev
                current.prev.next = None
            current = current.prev



llist = DoublyLinkedList()

wind = Tk()
wind.title("lab3")
wind.geometry('350x300')

def app():
    for i in enter2.get():
        llist.append(i)

def prep():
    for i in enter2.get():
        llist.append(i)

def rm():
    llist.remove(enter2.get())

def show():
    lbl3.configure(text = "your list: " + llist.print_list())

def ins():
    for i in enter3.get()[::-1]:
        llist.insert_after(enter4.get(), i)

def lab():
    llist.lab_function()

def lab2():
    array = list(enter5.get())
    i = 0
    while i < len(array):
        if array[i] in ("1","2","3","4","5","6","7","8","9","0"):
            array.remove(array[i])
            i -= 1
        elif(array[i] == "a"):
            array.insert(i, "a")
            i += 1
        i+=1
    i = len(array) - 1
    while i >= 0:
        if array[i] == ' ':
            array = array[:i]
            break
        i -= 1
    lbl4.configure(text = ' '.join(array))

lbl2 = Label(wind, text="enter key", width=30)
lbl2.grid()

enter2 = Entry(wind, width=20)
enter2.grid(column=0, row=1)

btn = Button(wind, text = "remove", fg = "red", command=rm)
btn.grid(column=1, row=0)

btn2 = Button(wind, text = "append", fg = "red", command=app)
btn2.grid(column=1, row=1)

btn3 = Button(wind, text = "prepend", fg = "red", command=prep)
btn3.grid(column=1, row=2)

btn4 = Button(wind, text = "lab", fg = "red", command=lab)
btn4.grid(column=1, row=3)

btn3 = Button(wind, text = "show", fg = "red", command=show)
btn3.grid(column=0, row=5)

lbl3 = Label(wind, text = "your list: " + llist.print_list())
lbl3.grid(column=0, row=6)

enter3 = Entry(wind, width=20)
enter3.grid(column=1, row=6)

btn4 = Button(wind, text = "insert after", fg = "red", command=ins)
btn4.grid(column=1, row=7)

enter4 = Entry(wind, width=20)
enter4.grid(column=1, row=8)

btn5 = Button(wind, text = "do", fg = "red", command=lab2)
btn5.grid(column=1, row=10)

enter5 = Entry(wind, width=20)
enter5.grid(column=0, row=10)

lbl4 = Label(wind, text = "with array method")
lbl4.grid(column=0, row=11)

wind.mainloop()