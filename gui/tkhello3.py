#coding=utf-8

import Tkinter

top = Tkinter.Tk()
hello = Tkinter.Label(top, text = 'Fuck gfw!')
hello.pack()

quit = Tkinter.Button(top, text = "presed to quit!",command = top.quit, bg='red', fg = 'white')
quit.pack(fill=Tkinter.X, expand=1)

Tkinter.mainloop()
