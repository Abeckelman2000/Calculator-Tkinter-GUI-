from tkinter import *
# the basic box frame window
root = Tk()
root.title("Calculator")

# entry/ input fields
Entry1 = Entry(root, width=35, borderwidth=5)
Entry1.grid(row=0, column=0, columnspan=4)

# globals
global var1
global math



# functions
    # enters the digit pressed
def buttonclick(number):
    current = Entry1.get()
    Entry1.delete(0, END)
    Entry1.insert(0, str(current) + str(number))
    return
    # clears out the input bar
def buttonClear():
    Entry1.delete(0, END)
    return

def buttonadd():
    global math
    global var1
    var1 = int(Entry1.get())
    math = "+"
    Entry1.delete(0, END)
    return

def buttonsub():
    global math
    global var1
    var1 = int(Entry1.get())
    math = "-"
    Entry1.delete(0, END)
    return

def buttonmul():
    global math
    global var1
    var1 = int(Entry1.get())
    math = "x"
    Entry1.delete(0, END)
    return

def buttondiv():
    global math
    global var1
    var1 = int(Entry1.get())
    math = "÷"
    Entry1.delete(0, END)
    return

def buttonequal():
    var2 = Entry1.get()
    Entry1.delete(0, END)
    # determining operation type
    if math == "+":
        Entry1.insert(0, var1 + int(var2))
    elif math == "-":
        Entry1.insert(0, var1 - int(var2))
    elif math == "x":
        Entry1.insert(0, var1 * int(var2))
    elif math == "÷":
        Entry1.insert(0, int(var1/int(var2)))
    else:
        Entry1.insert(0, "Error")




# buttons

    # creating 0-9 buttons
button1 = Button(root, text= "1", padx=40, pady=20, command=lambda: buttonclick(1))
button2 = Button(root, text= "2", padx=40, pady=20, command=lambda: buttonclick(2))
button3 = Button(root, text= "3", padx=40, pady=20, command=lambda: buttonclick(3))
button4 = Button(root, text= "4", padx=40, pady=20, command=lambda: buttonclick(4))
button5 = Button(root, text= "5", padx=40, pady=20, command=lambda: buttonclick(5))
button6 = Button(root, text= "6", padx=40, pady=20, command=lambda: buttonclick(6))
button7 = Button(root, text= "7", padx=40, pady=20, command=lambda: buttonclick(7))
button8 = Button(root, text= "8", padx=40, pady=20, command=lambda: buttonclick(8))
button9 = Button(root, text= "9", padx=40, pady=20, command=lambda: buttonclick(9))
button0 = Button(root, text= "0", padx=40, pady=20, command=lambda: buttonclick(0))

    # creating operation buttons
buttonEqual = Button(root, text= "=", padx=40, pady=20, command=buttonequal)
buttonClear = Button(root, text="Clear", padx= 29, pady= 20, command=buttonClear)
buttonAdd = Button(root, text= "+", padx=39, pady=20, command=buttonadd)
buttonSub = Button(root, text= "-", padx=41, pady=20, command=buttonsub)
buttonMul = Button(root, text= "x", padx=40, pady=20, command=buttonmul)
buttonDiv = Button(root, text= "÷", padx=39, pady=20, command=buttondiv)



    # numerical buttons
button1.grid(row= 1, column= 0)
button2.grid(row= 1, column= 1)
button3.grid(row= 1, column= 2)

button4.grid(row= 2, column= 0)
button5.grid(row= 2, column= 1)
button6.grid(row= 2, column= 2)

button7.grid(row= 3, column= 0)
button8.grid(row= 3, column= 1)
button9.grid(row= 3, column= 2)

button0.grid(row= 4, column= 0)
buttonClear.grid(row= 4, column= 1)
buttonEqual.grid(row= 4, column= 2)

    # operation buttons
buttonAdd.grid(row= 1, column= 3)
buttonSub.grid(row= 2, column= 3)
buttonMul.grid(row= 3, column= 3)
buttonDiv.grid(row= 4, column= 3)


root.mainloop()