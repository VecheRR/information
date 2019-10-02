from tkinter import *
import wmi
import win32net
import os
from tkinter import filedialog

class UserInformation(object):
    """ Class for comfortable work """

    def __init__(self):
        super(UserInformation, self).__init__()

        self.root = Tk()
        self.root.title('Information about users')
        self.root.resizable(0, 0)
        self.root.geometry('550x200+100+100')

        self.w = wmi.WMI()

        self.photo = PhotoImage(file = os.path.abspath('browse.png'))

        self.label = Label(self.root, text='Enter path to create file:', font=('Serif 18'))
        self.entry = Entry(self.root, width=35, font=("Calibri 18"))
        self.entry.insert(0, "C:/Users/veche/Desktop")
        self.browse = Button(self.root, image=self.photo, compound=LEFT, command=self.to_browse)
        self.btn = Button(self.root, text='OK', width=72, background="#008000", fg="#ffffff", command=self.out)

    def get_info(self, user):

        d = {

            'status' : str(win32net.NetUserGetLocalGroups (None, user.Name)),
            'name' : user.Name,
            'fullname' : user.FullName,
            'caption' : user.Caption,
            'description' : user.Description,
            'disabled' : user.Disabled,
            'domain' : user.Domain,
            'installdate' : user.InstallDate,
            'localaccount' : user.LocalAccount,
            'lockout' : user.Lockout,
            'passwordchangeable' : user.PasswordChangeable,
            'passwordexpires' : user.PasswordExpires,
            'passwordrequired' : user.PasswordRequired,

        }

        return d

    def out(self):

        self.path = self.entry.get() + '/' + 'Information.txt'
        self.f = open(self.path, 'w')
        self.f.write('status; ' + 'name; ' + 'fullname; ' + 'caption; ' + 'description; ' + 'disabled; ' + 'domain; ' + 'installdate; ' + 'localaccount; ' + 'lockout; ' + 'passwordchangeable; ' + 'passwordexpires; ' + 'passwordrequired; ' + "\n")

        for u in self.w.Win32_UserAccount():

            if u.Name in ['Администратор', 'Гость', 'DefaultAccount', 'WDAGUtilityAccount', 'Administrator', 'Admin', 'User', 'Gast', 'Standardkonto', 'StandardKonto']:
                continue

            self.new_dict = self.get_info(u)

            for key in self.new_dict:
                self.f.write(str(self.new_dict[key]) + '; ')

            self.f.write("\n")

        self.f.close()

    def pack(self):
        self.label.place(x=20, y=20)
        self.browse.place(x=465, y=78)
        self.entry.place(x=20, y=80)
        self.btn.place(x=20, y=140)

    def run(self):
        self.root.mainloop()

    def to_browse(self):
        self.new_path = filedialog.askdirectory()
        self.entry.delete(0, END)
        self.entry.insert(0, self.new_path)


a = UserInformation()
a.pack()
a.run()
