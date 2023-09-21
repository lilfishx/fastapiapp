from fastapi import FastAPI
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Boolean, sql, select, text, delete
from starlette.responses import HTMLResponse


app = FastAPI()

engine = create_engine("postgresql://postgres:postgres@localhost:5432/app", echo=True)

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("login", String(10), unique=True, nullable=False),
    Column("money_amount", Integer),
    Column("card_number", String(16), nullable=False),
    Column("status", Boolean(), server_default=sql.expression.true(), nullable=False)
)

passwords = Table(
    "passwords",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("password", String(10), nullable=False)
)

user_keys = ["id", "login", "card_amount", "card_number", "status"]

connection = engine.connect()

with open("init-db.sql") as file:
    query = text(file.read())
    connection.execute(query)


@app.get("/users", response_class=HTMLResponse)
def get_html():
    with open("html/users.html", encoding="UTF-8") as file:
        result = file.read()
        print(result)
        return result


@app.get("/", response_class=HTMLResponse)
def get_html():
    with open("html/index.html", encoding="UTF-8") as file:
        result = file.read()
        print(result)
        return result


@app.get("/by-id", response_class=HTMLResponse)
def get_html():
    with open("html/by-id.html", encoding="UTF-8") as file:
        result = file.read()
        print(result)
        return result


@app.get("/by-login", response_class=HTMLResponse)
def get_html():
    with open("html/by-login.html", encoding="UTF-8") as file:
        result = file.read()
        print(result)
        return result


@app.get("/api/users")
def get_users():
    query = select(users).where(users.c.status)
    result = connection.execute(query)
    return [{user_keys[i]: row[i] for i in range(4)} for row in result]


@app.get("/api/by-id")
def get_by_id(id: int):
    query = select(users).where(users.c.id == id)
    result = connection.execute(query)
    return [{user_keys[i]: row[i] for i in range(5)} for row in result]


@app.get("/api/by-login")
def get_by_id(login: str):
    query = select(users).where(users.c.login == login)
    result = connection.execute(query)
    return [{user_keys[i]: row[i] for i in range(5)} for row in result]


@app.on_event("shutdown")
def shutdown():
    users.drop(engine)
    passwords.drop(engine)
