#Importing modules
from tkinter import *

#basic display
root = Tk()
root.geometry("550x675")
#root.resizable(width=None, height=None)
root.configure(bg='#2c2e36')
root.title("Calculator")

#Result bar
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="agencyfb 40 bold", bg='#f2f7f7')
screen.pack(fill=X, ipadx=8, pady=20, padx=20)

#frame_1
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

frame_1 = Frame(root, bg='#2c2e36')
b_1 = Button(frame_1, text="7", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)
b_1 = Button(frame_1, text="8", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)
b_1 = Button(frame_1, text="9", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)
b_1 = Button(frame_1, text="C", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)

frame_1.pack()

frame_1 = Frame(root, bg='#2c2e36')
b_1 = Button(frame_1, text="4", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)
b_1 = Button(frame_1, text="5", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)
b_1 = Button(frame_1, text="6", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)
b_1 = Button(frame_1, text="+", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)

frame_1.pack()

frame_1 = Frame(root, bg='#2c2e36')
b_1 = Button(frame_1, text="1", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)
b_1 = Button(frame_1, text="2", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)
b_1 = Button(frame_1, text="3", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)
b_1 = Button(frame_1, text=" - ", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)

frame_1.pack()

frame_1 = Frame(root, bg='#2c2e36')
b_1 = Button(frame_1, text="0", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)

b_1 = Button(frame_1, text="×", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)

b_1 = Button(frame_1, text="÷", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)

b_1 = Button(frame_1, text="%", padx=18, pady=8, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)

frame_1.pack()

frame_1 = Frame(root, bg='#2c2e36')
b_1 = Button(frame_1, text="=", padx=18, pady=18, font="lucida 35 bold", bg="#000000", fg="#a3a3a3")
b_1.pack(side=LEFT, padx=18, pady=5)
b_1.bind("<Button-1>", click)

frame_1.pack()

root.mainloop()
