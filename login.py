########################################
########################################
########################################
#url = 'http://192.168.122.146:8069' 
#db = 'cacao'
#username = 'robincoello@hotmail.com'
#password = 'admin'
########################################
########################################
#url = 'https://edu-1800395.odoo.com' 
#db = 'edu-1800395'
#url = 'https://edu-1800183.odoo.com' 
#db = 'edu-1800183'
#username = 'roencosa@gmail.com'
#password = 'ses'
########################################

import xmlrpclib
import os
import json
import getpass
from Tkinter import *
#


def login():
    print("First Name: %s\nLast Name: %s" % (username, password))
    common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
    uid = common.authenticate(db, username.get(), password.get(), {})


    while uid:
        print'Login ok'
        win_master()
        break
    else:
        print "Login or pass error"




def win_master():
    window = Tk()
    window.title("Odoo Master")
    window.config(bg="white")
    window.geometry("600x300")
    widget = Label(window, text="ODOO Manager")
    widget.pack(expand=YES, fill=BOTH)
    window.mainloop()


def win_login():
    global username
    global password
    	
    window = Tk()
    window.title("Odoo Login")
    window.config(bg="white")
    window.geometry("600x300")


    Label(window, text="Username").grid(row=2)
    Label(window, text="Password").grid(row=3)

    username = Entry(window)
    password = Entry(window, show='*')


    username.grid(row=2, column=1)
    password.grid(row=3, column=1)


    Button(window, text='Quit', command=window.quit).grid(row=5, column=0, sticky=W, pady=4)
    Button(window, text='Show', command=login).grid(row=5, column=1, sticky=W, pady=4)

    window.mainloop()


win_login()












