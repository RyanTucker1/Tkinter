from Tkinter import * #gives us access to everything in the Tkinter class

root = Tk() #gives us a blank canvas object to work with
root.title("Here Comes the Dong")

button1 = Button(root, text="Button 1")
button1.grid(row=1, column=1)

entry1 = Entry(root)
entry1.grid(row=1, column=0)

label1 = Label(root, text="Owen Wilson", bg="pink",anchor=E)
label1.grid(row=0, column=0, sticky=EW)



mainloop() #causes the windows to display on the screen until program closes