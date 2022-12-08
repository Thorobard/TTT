

from tkinter import *
import sys
import os
from PIL import Image, ImageTk

root = Tk()

#root.state('zoomed')
def main():
    root.geometry("900x900")
    root.title("My First GUI")
    root.configure(background="black")
    label = Label (root, text="Hello World!", font=('Arial', 20), fg="white", background="black")
    label.pack(padx=10, pady=10)



    textbox = Text (root, height=1, background="black", font=('Arial', 20, ), fg="white")
    textbox.pack(padx=50, pady=50)
    my_entry = Entry (root, background="black", fg="white", font=(100), )
    my_entry.pack(padx=20, pady=20)

    button = Button(root, text=("Clicker!!!"), font=('Arial', 20), background="lightblue3")
    button.pack()

    button_frame = Frame(root)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)


    btn1 = Button(button_frame, text="1", font=('Arial', 20))
    btn1.grid(row=0, column=0, sticky=W+E)

    btn2 = Button(button_frame, text="2", font=('Arial', 20))
    btn2.grid(row=0, column=1, sticky=W+E)

    btn3 = Button(button_frame, text="3", font=('Arial', 20))
    btn3.grid(row=0, column=2, sticky=W+E)

    btn4 = Button(button_frame, text="4", font=('Arial', 20))
    btn4.grid(row=1, column=0, sticky=W+E )

    btn5 = Button(button_frame, text="5", font=('Arial', 20))
    btn5.grid(row=1, column=1, sticky=W+E)

    btn6 = Button(button_frame, text="6", font=('Arial', 20))
    btn6.grid(row=1, column=2, sticky=W+E)

    button_frame.pack(fill=X)

    photo1 = (Image.open("Assets\proxy-image.gif"))

    resized_photo1 = photo1.resize((500,505), Image.ANTIALIAS)
    new_photo1 = ImageTk.PhotoImage(resized_photo1)
    Label(root, image=new_photo1, bg="black").pack()


    root.mainloop()
if __name__ == "__main__":
    main()