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

import pandas 



print "Your password odoo (" + url + ")"
password = getpass.getpass()
table = "mrp.bom"

def rc_campos_bom():
    return {
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
def rc_campos_bom_line():
    return {
            'fields': [
            'id',
            'product_id',
            'product_qty',
            'product_uom_id',
            'sequence',
            'routing_id',
            'bom_id',
            'operation_id',            
            'create_uid',
            'create_date',
            'write_uid',
            'write_date'
                        ]
        }


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



def detalles(rc_id):
    print("**************************************")
   
   # ids = models.execute_kw(db, uid, password, 'mrp.bom.line' , 'search',[[['bom_id', '=', rc_id]]],)
    ids = models.execute_kw(db, uid, password, 'mrp.bom.line', 'search',[[]],)

    resultat = models.execute_kw(db, uid, password, 'mrp.bom.line', 'read',[ids], {
            'fields': [
            'id',
            'product_id',
            'product_qty',
            'product_uom_id',
            'sequence',
            'routing_id',
            'bom_id',
            'operation_id',            
            'create_uid',
            'create_date',
            'write_uid',
            'write_date'
                        ]
        })

# boucle para contar los productos
    total = 0
    for reg in resultat:
        total += 1
    
            
    #print "Customers list : "+str(resultat)

    print(json.dumps(resultat, indent=4))

    print("Total de productos: " + repr(total))


################################################################################
def list():
    print("**************************************")
   # ids = models.execute_kw(db, uid, password, table , 'search',[[['id', '=', True]]],)
   # ids = models.execute_kw(db, uid, password, table , 'search',[[['id', '=', 3]]],)
    ids = models.execute_kw(db, uid, password, table, 'search',[[]],)

    resultat = models.execute_kw(db, uid, password,table, 'read',[ids], rc_campos_bom())

# boucle para contar los productos
    total = 0
    for reg in resultat:
        total += 1
    
            
    #print "Customers list : "+str(resultat)

    print(json.dumps(resultat, indent=4))

    print("Total de productos: " + repr(total))

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

    resultat = models.execute_kw(db, uid, password, table, 'read',[ids], rc_campos()

    )
   # print "Customers list : "+str(resultat)
    print(json.dumps(resultat, indent=4))

def jsontoxls():    
    pandas.read_json("odoo.json").to_excel("odoo.xlsx")





def menu():
    print("******************************")
    print("********** S H O P ***********")
    print("******* M A N A G E R ********")
    print("******************************")
    print("* SHOP : " + url)
    print("* DB   : " + db)
    print("******************************") 
    print("** N O E N C L A T U R E S ***") 
    print("******************************") 
    print("1) List Nomenclatures")       
    print("3) Nomenclature details ")
  # print("5) Delete ")
  # print("6) Search")
#   print("0) Exit")
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
    print("List")
    jsontoxls() 
    list()

####################################################
####################################################
######### D E T A I L S  ###########################

if opcion == 3:
    print("**************************************")
    print("Details")
    rc_id = raw_input("ID number please ")
## D E T A I L S
    detalles(rc_id)
   




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
    
