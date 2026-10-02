from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = "fila.db"


# --------------------------------------------------
# CONEXÃO COM O BANCO
# --------------------------------------------------

def conectar_banco():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# --------------------------------------------------
# CRIAÇÃO DO BANCO
# --------------------------------------------------

def criar_banco():
    conn = conectar_banco()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            servico TEXT NOT NULL,
            horario DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'aguardando'
        )
    """)

    conn.commit()
    conn.close()


# --------------------------------------------------
# PÁGINA PRINCIPAL
# --------------------------------------------------

@app.route("/")
def index():

    conn = conectar_banco()

    clientes = conn.execute("""
        SELECT *
        FROM clientes
        ORDER BY id ASC
    """).fetchall()

    conn.close()

    return render_template("index.html", clientes=clientes)


# --------------------------------------------------
# CADASTRAR CLIENTE
# --------------------------------------------------

@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    nome = request.form["nome"]
    servico = request.form["servico"]

    conn = conectar_banco()

    conn.execute("""
        INSERT INTO clientes (nome, servico)
        VALUES (?, ?)
    """, (nome, servico))

    conn.commit()
    conn.close()

    return redirect(url_for("index"))


# --------------------------------------------------
# CHAMAR PRÓXIMO CLIENTE
# --------------------------------------------------

@app.route("/chamar", methods=["POST"])
def chamar():

    conn = conectar_banco()

    # Procura o cliente mais antigo que ainda está aguardando
    cliente = conn.execute("""
        SELECT *
        FROM clientes
        WHERE status = 'aguardando'
        ORDER BY id ASC
        LIMIT 1
    """).fetchone()

    if cliente:
        conn.execute("""
            UPDATE clientes
            SET status = 'atendimento'
            WHERE id = ?
        """, (cliente["id"],))

        conn.commit()

    conn.close()

    return redirect(url_for("index"))


# --------------------------------------------------
# ALTERAR STATUS
# --------------------------------------------------

@app.route("/status/<int:id>", methods=["POST"])
def alterar_status(id):

    novo_status = request.form["status"]

    status_validos = [
        "aguardando",
        "atendimento",
        "concluido"
    ]

    if novo_status not in status_validos:
        return redirect(url_for("index"))

    conn = conectar_banco()

    conn.execute("""
        UPDATE clientes
        SET status = ?
        WHERE id = ?
    """, (novo_status, id))

    conn.commit()
    conn.close()

    return redirect(url_for("index"))


# --------------------------------------------------
# CANCELAR ATENDIMENTO
# --------------------------------------------------

@app.route("/cancelar/<int:id>", methods=["POST"])
def cancelar(id):

    conn = conectar_banco()

    conn.execute("""
        UPDATE clientes
        SET status = 'cancelado'
        WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()

    return redirect(url_for("index"))


# --------------------------------------------------
# INICIAR SISTEMA
# --------------------------------------------------

if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)