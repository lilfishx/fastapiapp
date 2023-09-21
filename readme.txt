для запуска нужно:
установить postgresql + pgadmin

dbuser = postgres
dbpassword = postgres
dbhost = localhost
dbport=5432
создать базу данных app

в терминале pycharm ввести

pip install fastapi[all]
pip install sqlalchemy
pip install psycopg2

запуск

uvicorn main:app --reload

на localhost появится приложение