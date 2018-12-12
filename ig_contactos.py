#coding:utf-8
import xmlrpclib
import os
import json
import getpass
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
from tkMessageBox import *
from shutil import copyfile # donwload files
from datetime import timedelta
import random
from os import listdir # search files
from os.path import isfile, join # search files
import rc_file

################################################################################
## F U N C T I O N S ###########################################################
################################################################################
# login() 
# load_file()
# extraction()
# update()
# check_update()
# copy_file_to() Copy file from: to:
# ls() #list file in folder

# #############################################################################
def login():
    print("First Name: %s\nLast Name: %s" % (username, password))
    print("url: %s\nDB: %s" % (url, db))
    print "*************************************************************"
    print("Username: %s\nPassword: %s" % (username.get(), password.get()))
    print("url: %s\nDB: %s" % (url.get(), db.get()))

    common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url.get()))
    uid = common.authenticate(db.get(), username.get(), password.get(), {})

    while uid:
        print'Login ok'
        win_master()        
        break
    else:
        #print "Login or pass error"
        #print("First Name: %s\nLast Name: %s" % (username, password))
        #print("url: %s\nDB: %s" % (url, db))
        #print("Username: %s\nPassword: %s" % (username.get(), password.get()))
        #print("url: %s\nDB: %s" % (url.get(), db.get()))
        showerror('Oops!', 'Username and/or Password Not Found.')
# #############################################################################
def load_file():
    window = Tk()
    window.filename = tkFileDialog.askopenfilename(initialdir = "/home/robin/a",title = "Select file",
    filetypes = (    
    ("doc files","*.json"),
    ("doc files","*.csv"),
    ("doc files","*.xlsx"),
    ("all files","*.*")
                )
    )
    
    copy_file_to(window.filename, './' + str(random.randint(0, 99)) + '.json')
    print (window.filename)
    window.mainloop()

### E x t r a c t i o ##########################################################
def extraction():
    print "Extraction ok "
    showinfo('ok!', 'Extraction ok....')

### U p d a t e  ############################################################### 
def update():
    print "Update ok"
    print "Data base name:" + db.get()
    #showinfo('ok!', 'Update ok')

    uid = common.authenticate(db.get(), username.get(), password.get(), {})

    print("**************************************")
    #ids = models.execute_kw(db.get(), username.get(), password.get(),'res.partner', 'search',[[['customer', '=', True]]],)

    resultat = models.execute_kw(db.get(), username.get(), password.get(),
    'res.partner', 'read',[ids],
        {
            'fields': [
            'parent_id',
            'name',
            'mobil',
            'phone',
            'email',
            'street',
            'title' 
]
        }
    )
   # print "Customers list : "+str(resultat)
    print(json.dumps(resultat, indent=4))
    
### c h e c k u p d a t e #######################################################
def check_update():
    print "check update ok"
    showinfo('ok!', 'check update ok')

### c o p y f i l e  t o #######################################################
# https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python
def copy_file_to(src, dest): 
    copyfile(src, dest)
    #print("File :" + to)
# #############################################################################
# https://es.stackoverflow.com/questions/24278/c%C3%B3mo-listar-todos-los-archivos-de-una-carpeta-usando-python 
def ls(ruta = '.'):
    return [arch for arch in listdir(ruta) if isfile(join(ruta, arch))]
########## contacts.list() #############################################################################
def contacts_list():
    global db
    global uid
    global password
    global common
    print("**************************************")
    #ids = common.execute_kw(db, uid, password,'res.partner', 'search',[[['customer', '=', True]]],)

    resultat = common.execute_kw(db, uid, password,
    'res.partner', 'read',[ids],
        {
            'fields': [
            'parent_id',
            'name',
            'mobil',
            'phone',
            'email',
            'street',
            'title' 
]
        }
    )
   # print "Customers list : "+str(resultat)
    print(json.dumps(resultat, indent=4))    


################################################################################
## W I N D O W S ###############################################################
################################################################################
#
# win_master() Fenetre principal
# win_login() Fenetre pour le login 
#
#
#
def win_master():
    window = Tk()
    window.title("Odoo Contacts")
    window.config(bg="white")
    window.geometry("550x500+310+0")

    #Création des widgets
    label1 = Label(window, text="Nom du ficher Excel")
    label2 = Label(window, text="id du produit")
    
    btn1 = Button(window, text="List contacts", command=contacts_list)
    btn2 = Button(window, text="Extraction de données", command=extraction)
    btn3 = Button(window, text="muestra DB", command=update)
    btn4 = Button(window, text="Vérifier la mise a jour", command=check_update)
    btn5 = Button(window, text='QUITTER', command=window.quit)

    id_product = Entry(window)
    id_product.insert(END, '6')
    id_product.grid(row=7, column=1)  

    btn10 = Button(window, text="Genere ficher excel", command="")


    #Afficahge de tous les widgets et positionnements
    label1.grid(row=0, column=1, sticky=E)
    label2.grid(row=7,column=2, sticky=E)
    btn1.grid(row=0, column=0, padx=5, pady=20)
    btn2.grid(row=4, column=0, padx=5, pady=20)
    btn3.grid(row=5, column=0, padx=5, pady=20)
    btn4.grid(row=6, column=0, padx=5, pady=20)
    btn5.grid(row=8, column=0, padx=5, pady=20)
    btn10.grid(row=7, column=0, padx=5, pady=20)

    window.mainloop()

    
    
def win_login():
    global url
    global db
    global username
    global password
    	
    window = Tk()
    window.title("Odoo Login")
    window.config(bg="white")
    window.geometry("300x300+0+0")

    Label(window, text="Url Odoo").grid(row=0)
    Label(window, text="DB").grid(row=1)
    Label(window, text="Username").grid(row=2)
    Label(window, text="Password").grid(row=3)

    Label(window, text="Odoo Server").grid(row=0, column=3)



    url = Entry(window)
    url.insert(END, 'https://edu-1800395.odoo.com')

    db = Entry(window)
    db.insert(END, 'edu-1800395')

    username = Entry(window)
    username.insert(END, 'roencosa@gmail.com')

    password = Entry(window, show='*')
    password.insert(END, '102030')


    #Afficahge de tous les widgets et positionnements
    url.grid(row=0, column=1)
    db.grid(row=1, column=1)
    username.grid(row=2, column=1)
    password.grid(row=3, column=1)

    Button(window, text='Quit', command=window.quit).grid(row=5, column=0, sticky=W, pady=4)
    Button(window, text='Login', command=login).grid(row=5, column=1, sticky=W, pady=4)

    window.mainloop()


## Execution initial du code

win_login()













