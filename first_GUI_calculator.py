from tkinter import *


#Function for getting value on clicking
def on_click_function(value):
    global global_variable
    global_variable = global_variable + str(value)
    entry_var.set(global_variable)


#Function for evaluating the numbers with the help of string
def eval_function():
    global global_variable
    try:
        result = str(eval(global_variable))
        entry_var.set(result)
        global_variable = " "
    except:
        entry_var.set("Error ...!!!")


#Function for clearing the expression variable and seting it to ("") empty String 
def clear_function():
    global global_variable
    global_variable = ""
    entry_var.set(global_variable)


#Main GUI Code
root = Tk()
root.geometry("544x455")
root. resizable(0, 0)
root.title("!..Calculator..!")


#Frame for Entry widget of text field
frame1 = Frame(root, width=100, height=100, bd=1, highlightthickness=1, highlightbackground="lightgrey", highlightcolor="grey")
frame1.pack(side=TOP)

global_variable = ""
entry_var = StringVar()
entry_value = Entry( frame1, textvariable=entry_var, font="arial 25 bold",width=90, bg="#FFFFFF", fg="#000000" )
entry_value.grid(row=1, column=0)
entry_value.pack(ipady=42, ipadx=5)


#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------


#Frame for Buttons
frame2 = Frame(root, width=600, height=600, bd=5, bg="#000000")
frame2.pack()

# FIrst row 

clear_scr = Button(frame2, text="C", fg="black", height=3, width=30, foreground="white", bg="black", command=lambda: clear_function())
clear_scr.grid(row=0, column=0, columnspan=2, pady=10)

divide = Button(frame2, text="/", fg="black", height=3, width=30, foreground="white", bg="black", command=lambda: on_click_function("/"))
divide.grid(row=0, column=2, columnspan=2, pady=10)

#Second row

one = Button(frame2, text="1", fg="black", width=20, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda:on_click_function(1) )
one.grid(row=1, column=0)

two = Button(frame2, text="2", fg="black", width=20, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda:on_click_function(2))
two.grid(row=1, column=1)


three = Button(frame2, text="3", fg="black", width=20, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda:on_click_function(3))
three.grid(row=1, column=2)


plus = Button(frame2, text="+", fg="black", width=10, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda:on_click_function("+"))
plus.grid(row=1, column=3)



# Thrid row

four = Button(frame2, text="4", fg="black", width=20, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda:on_click_function(4))
four.grid(row=2, column=0)

five = Button(frame2, text="5", fg="black", width=20, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda:on_click_function(5))
five.grid(row=2, column=1)


six = Button(frame2, text="6", fg="black", width=20, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda:on_click_function(6))
six.grid(row=2, column=2)


minus = Button(frame2, text="-", fg="black", width=10, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda:on_click_function("-"))
minus.grid(row=2, column=3)


# Forth row

seven = Button(frame2, text="7", fg="black", width=20, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda:on_click_function(7))
seven.grid(row=3, column=0)

eight = Button(frame2, text="8", fg="black", width=20, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda:on_click_function(8))
eight.grid(row=3, column=1)


nine = Button(frame2, text="9", fg="black", width=20, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda:on_click_function(9))
nine.grid(row=3, column=2)


multi = Button(frame2, text="*", fg="black", width=10, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda:on_click_function("*"))
multi.grid(row=3, column=3)

# Fifty row

submit = Button(frame2, text="Submit", fg="lightgreen", width=20, height=3, font="Arial 9 bold", bg="red")
submit.grid(row=4, column=0)

zero = Button(frame2, text="0", fg="black", width=20, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda:on_click_function(0))
zero.grid(row=4, column=1)

equal = Button(frame2, text="=", fg="black", width=32, height=3, font="Arial 9 bold", foreground="white", bg="black", command= lambda: eval_function())
equal.grid(row=4, column=2, columnspan=2)

root.mainloop()