########################################
########################################
########################################
url = 'https://edu-1800395.odoo.com' 
db = 'edu-1800395'
username = 'roencosa@gmail.com'
password = '666666666666666666'

########################################
########################################
########################################

########################################
########################################
########################################
#url = 'http://192.168.122.146:8069' 
#db = 'shop'
#username = 'robincoello@hotmail.com'
#password = 'admin'
########################################
########################################
########################################

import xmlrpclib
import os
import json

import getpass

print "Your password odoo (" + url + ")"
password = getpass.getpass()
table = "mrp.bom"


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


def total_products():
    return models.execute_kw(db, uid, password,
    'res.partner', 'search_count',
    [[['is_company', '=', True], ['customer', '=', True]]])



def detalles(rc_id_product):
    print("**************************************")
    print("Product n: " + str(rc_id_product) +  " details")
    #rc_id_customer = raw_input("Customer number please ")

    ids = models.execute_kw(db, uid, password,
    'product.product', 'search',
    [[ ['id','=',rc_id_product]]],
    )

    resultat = models.execute_kw(db, uid, password,
    'product.product', 'read',[ids],
        {
            'fields': [
            'id',
            'default_code',
            'active',
            'product_tmpl_id',
            'barcode',
            'volume',
            'weight',
            'message_last_post',
            'activity_date_deadline',            
            'create_uid',
            'create_date',
            'write_uid',
            'write_date'
                        ]
        }
    



    )
   # print "Customers list : "+str(resultat)
    print(json.dumps(resultat, indent=4))

##############################################
##############################################
def search(rc_name):
    print("**************************************")
    print("Search for : " + rc_name )
    #rc_id_customer = raw_input("Customer number please ")

    ids = models.execute_kw(db, uid, password,
    'product.product', 'search',
    [[ ['name','=',rc_name]]],
    )

    resultat = models.execute_kw(db, uid, password,
    'product.product', 'read',[ids],
        {
            'fields': [
            'id',
            'default_code',
            'active',
            'product_tmpl_id',
            'barcode',
            'volume',
            'weight',
            'message_last_post',
            'activity_date_deadline',            
            'create_uid',
            'create_date',
            'write_uid',
            'write_date'
                        ]
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
    print("** P R O D U C T S ***********") 
    print("******************************") 
    print("1) List")   
    print("2) Add ")
    print("3) Details")
    print("4) Edit ")
    print("5) Delete ")
    print("6) Search")
#    print("0) Exit")
    print("")
    print("TAKE A NUMBER")


os.system('clear')
menu()


opcion = input()

while(opcion > 6 or opcion < 1 ):
    print("Please a number between 1 - 6")
    opcion = input()






if opcion == 111:
    print("**************************************")

    resultat = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[
        ['customer', '=', True],
        
    ]])
    print "List : "+str(resultat)

####################################################
######### L I S T ##################################
#
if opcion == 1:
    print("**************************************")
   # ids = models.execute_kw(db, uid, password, table , 'search',[[['id', '=', True]]],)
    ids = models.execute_kw(db, uid, password, table, 'search',[[]],)

    resultat = models.execute_kw(db, uid, password,
    table, 'read',[ids],
        {
            'fields': [
            'id',
            'code',
            'active',
            'type',
            'product_tmpl_id',
            'product_id',
            'product_qty',
            'product_uom_id',
            'sequence',
            'routing_id',
            'ready_to_produce',
            'picking_type_id',
            'company_id',
            'message_last_post',
            'create_uid',
            'create_date',
            'write_uid',
            'write_date'
                        ]
        }
    
    )

# boucle para contar los productos
    total = 0
    for reg in resultat:
        total += 1
    
            
    #print "Customers list : "+str(resultat)

    print(json.dumps(resultat, indent=4))

    print("Total de productos: " + repr(total))
####################################################
######### A D D #####################################
#
if opcion == 2:
    print("**************************************")
    print("Add a NEW")

    rcname      = raw_input("Name please: ")
   

    id = models.execute_kw(db, uid, password, 'product.product', 'create', [{
    'name'      : rcname,
   
    }])
    id = str(id)
    print(rcname + ' is add: ')
    detalles(id)

####################################################
######### D E T A I L S  ###########################

if opcion == 3:
    print("**************************************")
    print("Details")
    rc_id = raw_input("ID number please ")
## D E T A I L S
    detalles(rc_id)
   


####################################################
######### E D I T ##################################

if opcion == 4:
    print("**************************************")
    print("Edit")
    print("**************************************")
    rc_id = input("Customer number please: ")


## D E T A I L S
    detalles(rc_id)

    rc_name = raw_input("New name: ")
    

    models.execute_kw(db, uid, password, 'product.product', 'write', [[rc_id], {
        'name': rc_name

    }])
    # get record name after having changed it
    name = models.execute_kw(db, uid, password, 'product.product', 'name_get', [[rc_id]])
    if name:
        print('The item is update! ' )

    ## detalles(rc_id)



####################################################
######### D E L E T E ##############################

if opcion == 5:
    print("**************************************")
    print("Delete")

    rc_id = raw_input("Id to delete please: ")
    id = int(rc_id)
    models.execute_kw(db, uid, password, 'product.product', 'unlink', [[id]])
    # check if the deleted record is still in the database

    verif = models.execute_kw(db, uid, password,
        'product.product', 'search', [[['id', '=', id]]])
    if not verif:
        print('The item is delete for ever ! ')

    detalles(id)
####################################################
######### D E L E T E ##############################
if opcion == 10:
    print("**************************************")

    resultat = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[
        ['customer', '=', True],
        ['is_company', '=', True],
    ]])
    print "Companies list : "+str(resultat)


####################################################
######### S E A R C H  ###########################

if opcion == 6:
    print("**************************************")
    print("Search")
    rc_name = raw_input("Name please ")
## D E T A I L S
    search(rc_name)
    
