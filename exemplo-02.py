from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI

from typing import Optional
import strawberry 
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
	idade: int

# cria o banco de dados.
SQLModel.metadata.create_all(engine)


@strawberry.type
class Pessoa:
	id: Optional[int]
	nome: str
	idade: int

@strawberry.type
class Query:

	@strawberry.field
	def all_pessoas(self) -> list[Pessoa]:
		query = select(Person)
		with Session(engine) as session:
			result = session.execute(query).scalars().all()
		return result 


def create_pessoa(idade: int, nome: str):
	pessoa = Person(nome=nome, idade=idade)
	with Session(engine) as session:
		session.add(pessoa)
		session.commit()
		session.refresh(pessoa)
	return pessoa


@strawberry.type
class Mutation:
	create_pessoa: Pessoa = strawberry.field(resolver=create_pessoa)


schema = strawberry.Schema(query=Query, mutation=Mutation)


graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")