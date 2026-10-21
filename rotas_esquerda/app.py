from flask import Flask, redirect, render_template, request, url_for
from sqlalchemy import select

from database import SessionLocal
from models import Book, User

app = Flask(__name__)

@app.route("/")
def index():
    session = SessionLocal()
    usuarios = session.scalars(select(User).order_by(User.nome)).all()
    livros = session.scalars(select(Book).order_by(Book.titulo)).all()
   
    session.close()

    return render_template("index.html", usuarios=usuarios, livros=livros, usuario=None)

@app.route("/usuario/novo",methods=["POST","GET"])
def new_user():
    if request.method == "POST":
        nome = request.form.get("nome", None)
        email = request.form.get("email", None)

        if nome and email:
            session = SessionLocal()
            usuario = session.scalars(select(User).where(User.email==email))

            if not usuario:
                usuario_novo = User(nome=nome, email=email)
                session.add(usuario_novo)
                session.commit()

            session.close()
            return redirect(url_for('login'))
    return render_template("cadastro.html")

@app.route("/livros/novo", methods=["POST","GET"])
def new_book():
    session = SessionLocal()

    usuarios = session.scarlrs(select(User).order_by(User.nome))
    if request.method == "POST":
        titulo = request.form.get("titulo")
        user_id = request.form.get("user_id")

        if titulo and user_id:
            livro_novo = Book(titulo=titulo,user_id=int(user_id))

            session.add(livro_novo)
            session.commitr()
            session.close()
            return redirect(url_for("listar_livro"))

    session.close()

    return render_template("cadastro_livro.html", usuario = ursuario)

@app.route("/livros/listar")
def listar_livro():
    session = SessionLocal()
    livros = session.scalars(select(Book).order_by(Book.titulo)).all()
    
    session.close()

    return render_template("livros.html", livros=livros)


@app.route("/usuarios/listar")
def listar_usuarios():
    session = SessionLocal()
    usuarios = session.scalars(select(User).order_by(User.nome)).all()
    
    session.close()
    
    return render_template("index.html", usuarios=usuarios)


