для запуска нужно:

1)установить postgresql + pgadmin

dbuser = postgres
dbpassword = postgres
dbhost = localhost
dbport=5432
создать базу данных app

2)в терминале pycharm ввести

pip install fastapi[all]
pip install sqlalchemy
pip install psycopg2

запуск:

в терминале pycharm с проектом ввести

uvicorn main:app --reload

на localhost появится приложение
