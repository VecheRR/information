from tkinter import *
import platform
import os
import socket
import getpass

width = '400'
height = '400'
shift_x = '+100'
shift_y = '+100'

root = Tk()
root.title('Test')
root.geometry(width + 'x' + height + shift_x + shift_y)

info = platform.node()
info2 = getpass.getuser()
info3 = socket.gethostname()
info4 = os.getlogin()

Label(root, text=info[:-6]).pack()
Label(root, text=info2).pack()
Label(root, text=info4).pack()

root.mainloop()
