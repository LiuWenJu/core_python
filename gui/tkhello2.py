#coding=utf-8

import Tkinter

top = Tkinter.Tk()
quit = Tkinter.Button(top,text = 'pressed the button to quit!', command = top.quit)
quit.pack()
Tkinter.mainloop()
