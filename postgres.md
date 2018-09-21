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





## Listing Tables

```
cocoa=# \dt
```

Resultado

```
cocoa=# \dt
                              Liste des relations
 Schéma |                      Nom                      | Type  | Propriétaire 
--------+-----------------------------------------------+-------+--------------
 public | base_import_import                            | table | odoo
 public | base_import_tests_models_char                 | table | odoo
 public | base_import_tests_models_char_noreadonly      | table | odoo
 public | base_import_tests_models_char_readonly        | table | odoo
 public | base_import_tests_models_char_required        | table | odoo
 public | base_import_tests_models_char_states          | table | odoo
 public | base_import_tests_models_char_stillreadonly   | table | odoo
 public | base_import_tests_models_m2o                  | table | odoo
 public | base_import_tests_models_m2o_related          | table | odoo
 public | base_import_tests_models_m2o_required         | table | odoo
 public | base_import_tests_models_m2o_required_related | table | odoo
 public | base_import_tests_models_o2m                  | table | odoo
 public | base_import_tests_models_o2m_child            | table | odoo
 public | base_import_tests_models_preview              | table | odoo
 public | base_language_export                          | table | odoo
 public | base_language_import                          | table | odoo
 public | base_language_install                         | table | odoo
 public | base_module_configuration                     | table | odoo
 public | base_module_update                            | table | odoo
 public | base_module_upgrade                           | table | odoo
 public | base_update_translations                      | table | odoo
 public | change_password_user                          | table | odoo
 public | change_password_wizard                        | table | odoo
 public | ir_act_client                                 | table | odoo
 public | ir_act_report_xml                             | table | odoo
 public | ir_act_server                                 | table | odoo
 public | ir_act_url                                    | table | odoo
 public | ir_act_window                                 | table | odoo
 public | ir_act_window_group_rel                       | table | odoo
 public | ir_act_window_view                            | table | odoo
 public | ir_actions                                    | table | odoo
 public | ir_actions_todo                               | table | odoo
 public | ir_attachment                                 | table | odoo
 public | ir_config_parameter                           | table | odoo
 public | ir_config_parameter_groups_rel                | table | odoo
 public | ir_cron                                       | table | odoo
 public | ir_exports                                    | table | odoo
 public | ir_exports_line                               | table | odoo
 public | ir_filters                                    | table | odoo
 public | ir_logging                                    | table | odoo
 public | ir_mail_server                                | table | odoo
 public | ir_model                                      | table | odoo
 public | ir_model_access                               | table | odoo
 public | ir_model_constraint                           | table | odoo
 public | ir_model_data                                 | table | odoo
 public | ir_model_fields                               | table | odoo
 public | ir_model_fields_group_rel                     | table | odoo
 public | ir_model_relation                             | table | odoo
 public | ir_module_category                            | table | odoo
 public | ir_module_module                              | table | odoo
 public | ir_module_module_dependency                   | table | odoo
 public | ir_property                                   | table | odoo
 public | ir_rule                                       | table | odoo
 public | ir_sequence                                   | table | odoo
 public | ir_sequence_date_range                        | table | odoo
 public | ir_server_object_lines                        | table | odoo
 public | ir_translation                                | table | odoo
 public | ir_ui_menu                                    | table | odoo
 public | ir_ui_menu_group_rel                          | table | odoo
 public | ir_ui_view                                    | table | odoo
 public | ir_ui_view_custom                             | table | odoo
 public | ir_ui_view_group_rel                          | table | odoo
 public | ir_values                                     | table | odoo
 public | rel_modules_langexport                        | table | odoo
 public | rel_server_actions                            | table | odoo
 public | res_bank                                      | table | odoo
 public | res_company                                   | table | odoo
 public | res_company_users_rel                         | table | odoo
 public | res_config                                    | table | odoo
 public | res_config_installer                          | table | odoo
 public | res_config_settings                           | table | odoo
 public | res_country                                   | table | odoo
 public | res_country_group                             | table | odoo
 public | res_country_res_country_group_rel             | table | odoo
 public | res_country_state                             | table | odoo
 public | res_currency                                  | table | odoo
 public | res_currency_rate                             | table | odoo
 public | res_font                                      | table | odoo
 public | res_groups                                    | table | odoo
 public | res_groups_action_rel                         | table | odoo
 public | res_groups_implied_rel                        | table | odoo
 public | res_groups_report_rel                         | table | odoo
 public | res_groups_users_rel                          | table | odoo
 public | res_lang                                      | table | odoo
 public | res_partner                                   | table | odoo
 public | res_partner_bank                              | table | odoo
 public | res_partner_category                          | table | odoo
 public | res_partner_res_partner_category_rel          | table | odoo
 public | res_partner_title                             | table | odoo
 public | res_request_link                              | table | odoo
 public | res_users                                     | table | odoo
 public | res_users_log                                 | table | odoo
 public | rule_group_rel                                | table | odoo
 public | web_editor_converter_test                     | table | odoo
 public | web_editor_converter_test_sub                 | table | odoo
 public | web_planner                                   | table | odoo
 public | web_tour_tour                                 | table | odoo
 public | wizard_ir_model_menu_create                   | table | odoo
 public | wkf                                           | table | odoo
 public | wkf_activity                                  | table | odoo
 public | wkf_instance                                  | table | odoo
 public | wkf_transition                                | table | odoo
 public | wkf_triggers                                  | table | odoo
 public | wkf_witm_trans                                | table | odoo
 public | wkf_workitem                                  | table | odoo
(105 lignes)

```


## Tabla Extructure

```
cocoa=# \d res_partner
```

Resultado
```

                                             Table « public.res_partner »
         Colonne         |            Type             |                        Modificateurs                         
-------------------------+-----------------------------+--------------------------------------------------------------
 id                      | integer                     | non NULL Par défaut, nextval('res_partner_id_seq'::regclass)
 name                    | character varying           | 
 company_id              | integer                     | 
 comment                 | text                        | 
 website                 | character varying           | 
 create_date             | timestamp without time zone | 
 color                   | integer                     | 
 active                  | boolean                     | 
 street                  | character varying           | 
 supplier                | boolean                     | 
 city                    | character varying           | 
 display_name            | character varying           | 
 zip                     | character varying           | 
 title                   | integer                     | 
 country_id              | integer                     | 
 commercial_company_name | character varying           | 
 parent_id               | integer                     | 
 company_name            | character varying           | 
 employee                | boolean                     | 
 ref                     | character varying           | 
 email                   | character varying           | 
 is_company              | boolean                     | 
 function                | character varying           | 
 lang                    | character varying           | 
 fax                     | character varying           | 
 street2                 | character varying           | 
 barcode                 | character varying           | 
 phone                   | character varying           | 
 write_date              | timestamp without time zone | 
 date                    | date                        | 
 tz                      | character varying           | 
 write_uid               | integer                     | 
 customer                | boolean                     | 
 create_uid              | integer                     | 
 credit_limit            | double precision            | 
 user_id                 | integer                     | 
 mobile                  | character varying           | 
 type                    | character varying           | 
 partner_share           | boolean                     | 
 vat                     | character varying           | 
 state_id                | integer                     | 
 commercial_partner_id   | integer                     | 
Index :
    "res_partner_pkey" PRIMARY KEY, btree (id)
    "res_partner_commercial_partner_id_index" btree (commercial_partner_id)
    "res_partner_company_id_index" btree (company_id)
    "res_partner_date_index" btree (date)
    "res_partner_display_name_index" btree (display_name)
    "res_partner_name_index" btree (name)
    "res_partner_parent_id_index" btree (parent_id)
    "res_partner_ref_index" btree (ref)
Contraintes de vérification :
    "res_partner_check_name" CHECK (type::text = 'contact'::text AND name IS NOT NULL OR type::text <> 'contact'::text)
Contraintes de clés étrangères :
    "res_partner_commercial_partner_id_fkey" FOREIGN KEY (commercial_partner_id) REFERENCES res_partner(id) ON DELETE SET NULL
    "res_partner_company_id_fkey" FOREIGN KEY (company_id) REFERENCES res_company(id) ON DELETE SET NULL
    "res_partner_country_id_fkey" FOREIGN KEY (country_id) REFERENCES res_country(id) ON DELETE RESTRICT
    "res_partner_create_uid_fkey" FOREIGN KEY (create_uid) REFERENCES res_users(id) ON DELETE SET NULL
    "res_partner_parent_id_fkey" FOREIGN KEY (parent_id) REFERENCES res_partner(id) ON DELETE SET NULL
    "res_partner_state_id_fkey" FOREIGN KEY (state_id) REFERENCES res_country_state(id) ON DELETE RESTRICT
    "res_partner_title_fkey" FOREIGN KEY (title) REFERENCES res_partner_title(id) ON DELETE SET NULL
    "res_partner_user_id_fkey" FOREIGN KEY (user_id) REFERENCES res_users(id) ON DELETE SET NULL
    "res_partner_write_uid_fkey" FOREIGN KEY (write_uid) REFERENCES res_users(id) ON DELETE SET NULL
Référencé par :
    TABLE "res_company" CONSTRAINT "res_company_partner_id_fkey" FOREIGN KEY (partner_id) REFERENCES res_partner(id) ON DELETE SET NULL
    TABLE "res_partner_bank" CONSTRAINT "res_partner_bank_partner_id_fkey" FOREIGN KEY (partner_id) REFERENCES res_partner(id) ON DELETE CASCADE
    TABLE "res_partner" CONSTRAINT "res_partner_commercial_partner_id_fkey" FOREIGN KEY (commercial_partner_id) REFERENCES res_partner(id) ON DELETE SET NULL
    TABLE "res_partner" CONSTRAINT "res_partner_parent_id_fkey" FOREIGN KEY (parent_id) REFERENCES res_partner(id) ON DELETE SET NULL
    TABLE "res_partner_res_partner_category_rel" CONSTRAINT "res_partner_res_partner_category_rel_partner_id_fkey" FOREIGN KEY (partner_id) REFERENCES res_partner(id) ON DELETE
 CASCADE
    TABLE "res_users" CONSTRAINT "res_users_partner_id_fkey" FOREIGN KEY (partner_id) REFERENCES res_partner(id) ON DELETE RESTRICT

cocoa=# 

```




HELPS 

https://chartio.com/resources/tutorials/how-to-list-databases-and-tables-in-postgresql-using-psql/