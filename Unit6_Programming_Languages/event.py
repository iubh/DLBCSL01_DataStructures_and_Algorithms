from tkinter import *
def clickButton():
    print("Button Clicked")

w = Tk()
l = Label(w, \
          text = "Event Driven Programming")
b = Button(w, \
           text = "Click here",command=clickButton)
l.pack()
b.pack()
w.mainloop()
