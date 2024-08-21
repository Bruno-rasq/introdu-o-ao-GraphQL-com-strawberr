from sqlmodel import Session, select
from .models import engine, Pessoa, Livro


def post_pessoa(idade: int, nome: str):
	pessoa = Pessoa(nome=nome, idade=idade)
	with Session(engine) as session:
		session.add(pessoa)
		session.commit()
		session.refresh(pessoa)
	return pessoa


def post_livro(titulo: str, pessoa_id: int):
	livro = Livro(titulo=titulo, pessoa_id=pessoa_id)
	with Session(engine) as session:
		session.add(livro)
		session.commit()
		session.refresh(livro)
	return livro


def get_pessoas(
	id: int = None,
	idade: int = None,
	limit: int = 5
):
	query = select(Pessoa)
	
	if id:
		query = query.where(Pessoa.id == id)
	if idade:
		query = query.where(Pessoa.idade == idade)
	if limit:
		query = query.limit(limit)
		
	with Session(engine) as session:
		result = session.execute(query).scalars().all()
	return result 


def get_livros():
	query = select(Livro).options(joinedload("*"))
	with Session(engine) as session:
		result = session.execute(query).scalars().unique().all()
	return result