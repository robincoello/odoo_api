########################################
########################################
########################################
#url = 'http://192.168.122.146:8069' 
#db = 'cacao'
#username = 'robincoello@hotmail.com'
#password = 'admin'
########################################
########################################
url = 'https://edu-1800395.odoo.com' 
db = 'edu-1800395'
username = 'roencosa@gmail.com'
#password = '1254541'
########################################

import xmlrpclib
import os
import json
import getpass

print "Your password odoo (" + url + ")"
password = getpass.getpass()

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print common.version()
uid = common.authenticate(db, username, password, {})

print uid
#print "******************************"


common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()
#print common.version()

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
models.execute_kw(
    db, 
    uid, 
    password,
    'res.partner', 
    'check_access_rights',
    ['read'], {'raise_exception': False})

def total_customers():
    return models.execute_kw(db, uid, password,
    'res.partner', 'search_count',
    [[['is_company', '=', True], ['customer', '=', True]]])



def detalles(rc_id_customer):
    print("**************************************")
    print("Cliente n: " + str(rc_id_customer) +  " details")
    #rc_id_customer = raw_input("Customer number please ")
    ids = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['customer', '=', True], ['id','=',rc_id_customer]]],
    )

    resultat = models.execute_kw(db, uid, password,
    'res.partner', 'read',[ids],
        {
            'fields': [
            'name',
            'company_id', 
            'parent_id',
            'mobil',
            'phone',
            'email',
            'street',
            'title' ]
        }
    )
   # print "Customers list : "+str(resultat)
    print(json.dumps(resultat, indent=4))


def menu():
    print("******************************")
    print("********** S H O P ***********")
    print("******* M A N A G E R ********")
    print("******************************")
    print("* SHOP : " + url)
    print("* DB   : " + db)
    print("******************************") 
    print("** C O N T A C T S ***********") 
    print("******************************") 
    print("1) List Contacts")
    print("2) Add Contact")
    print("3) View Contact")
    print("4) Edit Contact")
    print("5) Delete Contact")
#    print("0) Exit")
    print("")
    print("TAKE A NUMBER")


os.system('clear')
menu()


opcion = input()

while(opcion > 5 or opcion < 1 ):
    print("Please a number between 1 - 5")
    opcion = input()






if opcion == 111:
    print("**************************************")

    resultat = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[
        ['customer', '=', True],
        
    ]])
    print "Customers list : "+str(resultat)

####################################################
######### S H O W ##################################
#
if opcion == 1:
    print("**************************************")
    ids = models.execute_kw(db, uid, password,'res.partner', 'search',[[['customer', '=', True]]],)

    resultat = models.execute_kw(db, uid, password,
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

####################################################
######### A D D #####################################
#
if opcion == 2:
    print("**************************************")
    print("Add a NEW contact")

    rcname      = raw_input("Name please: ")
    rcphone     = raw_input("Phone number? ")
    rcparent_id = raw_input("In company number? ")
    rccity      = raw_input("City? ")
    rcstreet    = raw_input("Street? ")
    rczip       = raw_input("Zip? ")


    id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name'      : rcname,
    'phone'     : rcphone,
    'parent_id' :rcparent_id,
    'city'      :rccity,
    'street'    :rcstreet,
    'zip'       :rczip,

    }])
    id = str(id)
    print('The customer ' + id + ' is add: ')
    detalles(id)

####################################################
######### D E T A I L S  ###########################

if opcion == 3:
    print("**************************************")
    print("Contact details")
    rc_id_customer = raw_input("Customer number please ")
## D E T A I L S
    detalles(rc_id_customer)
    


####################################################
######### E D I T ##################################

if opcion == 4:
    print("**************************************")
    print("Contact Edit")
    print("**************************************")
    rc_id_customer = input("Customer number please: ")


## D E T A I L S
    detalles(rc_id_customer)

    rc_name = raw_input("New name: ")
    rc_phone = raw_input("New phone: ")

    models.execute_kw(db, uid, password, 'res.partner', 'write', [[rc_id_customer], {
        'name': rc_name,
        'phone': rc_phone

    }])
    # get record name after having changed it
    name = models.execute_kw(db, uid, password, 'res.partner', 'name_get', [[rc_id_customer]])
    if name:
        print('The customer is update! ' )

    ## detalles(rc_id_customer)



####################################################
######### D E L E T E ##############################

if opcion == 5:
    print("**************************************")
    print("Delete a contact")

    rc_id_customer = raw_input("Customer number to delete please: ")
    id = int(rc_id_customer)
    models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[id]])
    # check if the deleted record is still in the database

    verif = models.execute_kw(db, uid, password,
        'res.partner', 'search', [[['id', '=', id]]])
    if not verif:
        print('The customer is delete for ever ! ')

    detalles(id)

if opcion == 10:
    print("**************************************")

    resultat = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[
        ['customer', '=', True],
        ['is_company', '=', True],
    ]])
    print "Companies list : "+str(resultat)

