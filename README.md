# django-pg-research
Sample app for attempts dealing with new functions in djanog for PostgreSQL

Installation
---------

    $ pip install requirements.pip
    $ python manage.py generate
    $ python manage.py runserver


*Then you could open browser: http://localhost:8000/ and check some query results*


Explanation and Results
---------

DB schema in postgresql:

                           List of relations
     Schema |               Name                |   Type   | Owner  
    --------+-----------------------------------+----------+--------
     public | app_post                          | table    | andrey
     public | app_post_id_seq                   | sequence | andrey
     public | app_tag                           | table    | andrey
     public | app_tag_id_seq                    | sequence | andrey
     public | auth_group                        | table    | andrey
     public | auth_group_id_seq                 | sequence | andrey
     public | auth_group_permissions            | table    | andrey
     public | auth_group_permissions_id_seq     | sequence | andrey
     public | auth_permission                   | table    | andrey
     public | auth_permission_id_seq            | sequence | andrey
     public | auth_user                         | table    | andrey
     public | auth_user_groups                  | table    | andrey
     public | auth_user_groups_id_seq           | sequence | andrey
     public | auth_user_id_seq                  | sequence | andrey
     public | auth_user_user_permissions        | table    | andrey
     public | auth_user_user_permissions_id_seq | sequence | andrey
     public | django_admin_log                  | table    | andrey
     public | django_admin_log_id_seq           | sequence | andrey
     public | django_content_type               | table    | andrey
     public | django_content_type_id_seq        | sequence | andrey
     public | django_migrations                 | table    | andrey
     public | django_migrations_id_seq          | sequence | andrey
     public | django_session                    | table    | andrey
    (23 rows)

Post model:

                           Table "public.app_post"
       Column    |          Type          |                       Modifiers                       
    -------------+------------------------+-------------------------------------------------------
     id          | integer                | not null default nextval('app_post_id_seq'::regclass)
     name        | character varying(200) | not null
     description | text                   | not null
     tags        | integer[]              | 
    Indexes:
        "app_post_pkey" PRIMARY KEY, btree (id)
        "app_post_name_key" UNIQUE CONSTRAINT, btree (name)
        "app_post_name_a53642931e0f6d2_like" btree (name varchar_pattern_ops)

SQL Query "overlap":

    SELECT "app_post"."id", "app_post"."name", "app_post"."description", "app_post"."tags" 
    FROM "app_post" WHERE "app_post"."tags" && ARRAY[453, 378, 356, 358, 331]::integer[]

Time:

    Post amount: ~50000
    Tags amount: ~15000
    
    Without any index    
    Query time: ~23ms
    
    With btree index    
    Query time: ~18ms    
    
    With GIN index    
    Query time: ~1.5ms
    