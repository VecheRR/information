from tkinter import *
import platform
import os
import socket
import getpass
import sys
import subprocess
import win32net
import win32netcon
import time
import wmi

w = wmi.WMI()

for u in w.Win32_UserAccount(): # Net
    print (u.Name + ' -> ' + str(win32net.NetUserGetLocalGroups(None, u.Name)))

width = '500'
height = '500'
shift_x = '+100'
shift_y = '+50'

root = Tk() # create a main window
root.title('Test')
root.geometry(width + 'x' + height + shift_x + shift_y) # geometry of window

###############################################################################

myhost = socket.gethostname() # get hostname

Label(root, text='Hostname:').place(x=10, y=10)
e_host = Entry(root, width=50)
e_host.insert(0, myhost)
e_host.place(x=110, y=10)

###############################################################################

name = getpass.getuser() # get username

# win32net.NetGroupAdd(None, 0, 'TMPGroup')
# win32net.NetGroupAddUser(None, 'TMPGroup', name)

print(win32net.NetGroupGetInfo(None, 'TMPGroup', 0))

Label(root, text='Name of user:').place(x=10, y=50)
e_username = Entry(root, width=50)
e_username.insert(0, name)
e_username.place(x=110, y=50)

###############################################################################

info = platform.platform()

Label(root, text='Information:').place(x=10, y=90)
e_info = Entry(root, width=50)
e_info.insert(0, info)
e_info.place(x=110, y=90)

###############################################################################



###############################################################################

# root.mainloop()
