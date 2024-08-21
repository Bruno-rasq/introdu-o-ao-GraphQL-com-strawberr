import strawberry 
from typing import Optional, List
from strawberry.fastapi import GraphQLRouter
from .db_functions import post_pessoa, post_livro, get_pessoas, get_livros


@strawberry.type
class Pessoa:
	id: Optional[int]
	nome: str
	idade: int
	livros: List['Livro']
	
@strawberry.type
class Livro:
	id: Optional[int]
	titulo: str
	pessoa: Pessoa
	

@strawberry.type
class Query:
	all_pessoas: list[Pessoa] = strawberry.field(resolver=get_pessoas)
	all_livros: list[Livro] = strawberry.field(resolver=get_livros)

@strawberry.type
class Mutation:
	create_pessoa: Pessoa = strawberry.field(resolver=post_pessoa)
	create_livro: Livro = strawberry.field(resolver=post_livro)


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)