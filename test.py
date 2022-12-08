from tkinter import *

root = Tk()
root.geometry('250x150')

button1 = Button(text="Left")
button1.pack(side = LEFT)

button2 = Button(text="Top")
button2.pack(side = TOP)

button3 = Button(text="Right")
button3.pack(side = RIGHT)

button4 = Button(text="Bottom")
button4.pack(side = BOTTOM, fill=BOTH)

root.mainloop()