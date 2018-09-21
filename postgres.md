# postgres

Conection 

```
sudo -s
su – postgres
psql
```

psql (9.5.6) Digite «help» para obtener ayuda.

postgres=#



## Listing DataBase

```
postgres=# \l
```

Resultado:

```
postgres=# \l
                                  Liste des bases de données
    Nom    | Propriétaire | Encodage | Collationnement | Type caract. |    Droit
s d'accès     
-----------+--------------+----------+-----------------+--------------+---------
--------------
 cocoa     | odoo         | UTF8     | fr_BE.UTF-8     | fr_BE.UTF-8  | 
 odoo_db   | odoo_user    | UTF8     | fr_BE.UTF-8     | fr_BE.UTF-8  | 
 odoodb    | odoouser     | UTF8     | fr_BE.UTF-8     | fr_BE.UTF-8  | 
 postgres  | postgres     | UTF8     | fr_BE.UTF-8     | fr_BE.UTF-8  | 
 template0 | postgres     | UTF8     | fr_BE.UTF-8     | fr_BE.UTF-8  | =c/postg
res          +
           |              |          |                 |              | postgres
=CTc/postgres
 template1 | postgres     | UTF8     | fr_BE.UTF-8     | fr_BE.UTF-8  | =c/postg
res          +
           |              |          |                 |              | postgres
=CTc/postgres
(6 lignes)

```

## Switching Databases

```
postgres=# \c cocoa
```
Resultado
```
postgres=# \dc cocoa
               Liste des conversions
 Schéma | Nom | Source | Destination | Par défaut ? 
--------+-----+--------+-------------+--------------
(0 ligne)

postgres=# \c cocoa
Vous êtes maintenant connecté à la base de données « cocoa » en tant qu'utilisateur « postgres ».
cocoa=# 
```


HELPS 

https://chartio.com/resources/tutorials/how-to-list-databases-and-tables-in-postgresql-using-psql/