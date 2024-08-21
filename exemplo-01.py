from typing import Optional
from fastapi import FastAPI
from sqlmodel import (
	SQLModel,
	Field,
	create_engine,
	select,
	Session
)

#criar engine do banco
engine = create_engine("sqlite:///database.db")

class Person(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	nome: str
	idade: str

# cria o banco de dados.
SQLModel.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
def root():
	return {"message": "ok"}


@app.get("/pessoas")
def get_pessoas():
	query = select(Person)
	with Session(engine) as session:
		result = session.execute(query).scalars().all()
	return result 


@app.get("/pessoas-nome")
def get_pessoas():
	query = select(Person.nome)
	with Session(engine) as session:
		result = session.execute(query).scalars().all()
	return result 


@app.get("/pessoas-idade")
def get_pessoas():
	query = select(Person.idade)
	with Session(engine) as session:
		result = session.execute(query).scalars().all()
	return result 


@app.post("/user")
def create_user(id: int, nome: str, idade: int):
	pessoa = Person(id=id, nome=nome, idade=idade)
	with Session(engine) as session:
		session.add(pessoa)
		session.commit()
	return pessoa