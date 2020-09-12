from tkinter import *

win = Tk()
win.title("Calculator")

e1 = Entry(win, width=30, borderwidth=5, font="Calibri 12")
e1.grid(row=0, column=0, columnspan=5)
e1.get()

def click(num):
	e1.insert(END, num)

def button_equals():
	s_num = e1.get()
	e1.delete(0, END)

	if math == "addition":
		result = f_num + float(s_num)
		e1.insert(0, result)
	elif math == "subtraction":
		result = f_num - float(s_num)
		e1.insert(0, result)
	elif math == "multiplication":
		result = f_num * float(s_num)
		e1.insert(0, result)
	else:
		result = f_num / float(s_num)
		e1.insert(0, result)


def add():
	first_number = e1.get()
	global f_num 
	global math 
	math = "addition"
	f_num = float(first_number)
	e1.delete(0,END)

def delete():
	e1.delete(len(e1.get())-1)  # To delete last number of the entry widget

def Clear():
	e1.delete(0, END)  

def sub():
	first_number = e1.get()
	global f_num 
	global math 
	math = "subtraction"
	f_num = float(first_number)
	e1.delete(0,END)

def multiply():
	first_number = e1.get()
	global f_num 
	global math 
	math = "multiplication"
	f_num = float(first_number)
	e1.delete(0,END)


def divide():
	first_number = e.get()
	global f_num 
	global math 
	math = "division"
	f_num = float(first_number)
	e.delete(0,END)

def decimal():
	e1.insert(END, '.')


b1 = Button(win, text=1, fg="green", padx=20, pady=20, command=lambda:click(1))
b2 = Button(win, text=2, fg="green", padx=20, pady=20, command=lambda:click(2))
b3 = Button(win, text=3, fg="green", padx=20, pady=20, command=lambda:click(3))
b4 = Button(win, text=4, fg="green", padx=20, pady=20, command=lambda:click(4))
b5 = Button(win, text=5, fg="green", padx=20, pady=20, command=lambda:click(5))
b6 = Button(win, text=6, fg="green", padx=20, pady=20, command=lambda:click(6))
b7 = Button(win, text=7, fg="green", padx=20, pady=20, command=lambda:click(7))
b8 = Button(win, text=8, fg="green", padx=20, pady=20, command=lambda:click(8))
b9 = Button(win, text=9, fg="green", padx=20, pady=20, command=lambda:click(9))
b0 = Button(win, text=0, fg="green", padx=20, pady=20, command=lambda:click(0))
b_equal = Button(win, text='=', fg="green", padx=55, pady=20, command=button_equals)
b_del = Button(win, text='Delete', fg="green", padx=7, pady=20, command=delete)
b_add = Button(win, text='+', fg="green", padx=20, pady=5, command=add, font="Calibri 20")
b_sub = Button(win, text='-', fg="green", padx=20, pady=5, command=sub, font="Calibri 20")
b_mult = Button(win, text='x', fg="green", padx=20, pady=5, command=multiply, font="Calibri 20")
b_div = Button(win, text='/', fg="green", padx=20, pady=5, command=divide, font="Calibri 20")
b_clear = Button(win, text='Clear', fg="green", padx=45, pady=20, command=Clear)
b_decimal = Button(win, text='.', fg="green", padx=20, pady=0, command=decimal, font="Calibri 24")

b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b0.grid(row=4, column=0)
b_equal.grid(row=4, column=1, columnspan=2)
b_del.grid(row=5, column=0)
b_clear.grid(row=5, column=1, columnspan=2)
b_add.grid(row=5, column=3)
b_sub.grid(row=4, column=3)
b_mult.grid(row=3, column=3)
b_div.grid(row=2, column=3)
b_decimal.grid(row=1, column=3)

win.mainloop()