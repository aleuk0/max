from tkinter import *

a,b = 1000000,1

def new_guess(event):
    global a, b
    a,b = 1000000,1
    label.configure(text = "Guess numbers from 1 to 1000000. Number < 500000?")

def yes(event):
    global a, b
    a = ((a+b)/2)
    label.configure(text = ("Number < " + str(round((a+b)/2, 2)) + "?"))
    if round(a)==round(b):
        label.configure(text = ("Your number is " + str(round(a))))

def no(event):
    global a, b
    b = ((a+b)/2)
    label.configure(text = ("Number < " + str(round((a+b)/2, 2)) + "?"))
    if round(a)==round(b):
        label.configure(text = ("Your number is " + str(round(a))))

root = Tk()
root.title("Guess of number")
root.geometry('300x100+300+225')

button_yes = Button(root,text="ДА")
button_no = Button(root,text="НЕТ")
button_new_guess = Button(root,text="НОВЫЙ ПОИСК")

label = Label(root, width = 100)

button_yes.bind("<Button-1>",yes)
button_no.bind("<Button-1>",no)
button_new_guess.bind("<Button-1>",new_guess)

button_new_guess.pack(side='top')
label.pack(side='top')
button_yes.pack(side='left',
                fill = BOTH,
                expand = YES)
button_no.pack(side='right',
                fill = BOTH,
                expand = YES)

root.mainloop()
