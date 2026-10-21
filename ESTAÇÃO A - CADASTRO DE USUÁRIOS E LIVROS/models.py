from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int]               = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str]             = mapped_column(String, nullable=False)
    email: Mapped[str]            = mapped_column(String(120), unique=True)
    books: Mapped[list["Book"]] = relationship("Book", back_populares = "user")

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int]            = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str]        = mapped_column(String, nullable=False, unique=True)
    user_id: Mapped[int]    = mapped_column(Integer, ForeignKey("usuarios.id"), nullable=False) # Chave estrangeira para o banco de dados
    user: Mapped["User"] = relationship("User", back_populates = "books")