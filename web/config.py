DEV_DB = 'sqlite:///appnoo.db'

pg_user = 'postgres'
pg_pass = 'postgres'
pg_db = 'appnoo'
pg_host = 'db'
pg_port = 5432

PROD_DB = f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'
