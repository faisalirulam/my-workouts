from tkinter import *

window=Tk()
window.geometry("500x500")
window.title("Calculator")
window.configure(bg="red")

def hello():
    print("button created")


button=Button(text="ok",width=10,height=5,bg="black",fg="white", command=hello)
button2=Button(text="ok",width=10,height=5,bg="black",fg="white")
label=Label(window,text="welcome")

button.pack()
button2.pack()
label.pack()

window.mainloop()



