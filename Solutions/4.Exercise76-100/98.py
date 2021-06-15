from tkinter import *

window = Tk()

file = open("user_gui.txt", "a+")

user_value = StringVar()
entry = Entry(window, textvariable = user_value)
entry.grid(row= 0, column= 0)


def Add():
    file.write(user_value.get() + "\n")
    entry.delete(0, END)  # this clears the input box once add button is pressed


def Save():  # closes the file and opens again
    global file
    file.close()
    file = open("user_gui.txt", "a+")
def Close():
    file.close()
    window.destroy()


add_btn = Button(window, text= "Add", command= Add)

add_btn.grid(row=0, column=1)

save_btn = Button(window, text= "Save", command= Save)
save_btn.grid(row=0, column=2)

close_btn = Button(window, text= "Close", command= Close)
close_btn.grid(row=0, column=3)



window.mainloop()