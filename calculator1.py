from tkinter import *

root = Tk()
root.title("Simple Calculator")

# creating an entry box

entry_box = Entry(root, width=41, borderwidth=5)
entry_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click():
    return

def button_equal():
    return

def button_clear():
    return


button1 = Button(root, text="1", padx=35, pady=15, command=button_click)
button2 = Button(root, text="2", padx=35, pady=15, command=button_click)
button3 = Button(root, text="3", padx=35, pady=15, command=button_click)
button4 = Button(root, text="4", padx=35, pady=15, command=button_click)
button5 = Button(root, text="5", padx=35, pady=15, command=button_click)
button6 = Button(root, text="6", padx=35, pady=15, command=button_click)
button7 = Button(root, text="7", padx=35, pady=15, command=button_click)
button8 = Button(root, text="8", padx=35, pady=15, command=button_click)
button9 = Button(root, text="9", padx=35, pady=15, command=button_click)
button0 = Button(root, text="0", padx=35, pady=15, command=button_click)
buttonequal = Button(root, text="=", padx=77, pady=15, command=button_equal)
buttonadd = Button(root, text="+", padx=42, pady=15, command=button_equal)
buttonsub = Button(root, text="-", padx=44, pady=15, command=button_equal)
buttonmulti = Button(root, text="*", padx=42, pady=15, command=button_equal)
buttonclear = Button(root, text="Clear All", padx=20, pady=15, command=button_clear)


button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonequal.grid(row=4, column=1, columnspan=2)

buttonclear.grid(row=1, column=3)
buttonadd.grid(row=2, column=3)
buttonsub.grid(row=3, column=3)
buttonmulti.grid(row=4, column=3)

root.mainloop()
