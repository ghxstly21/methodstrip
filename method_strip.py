from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("MethodStrip")

icon = PhotoImage(file = "images/methodstrip_logo.png")
window.iconphoto(True, icon)
window.config(background = "#b4d6b9")

title = Label(window,
              text="MethodStrip",
              font=('Courier New', 40, 'bold'),
              bg="#b4d6b9",
              fg="black",
              relief="raised",
              bd=10)
title.place(x=210, y=105)

window.mainloop()
