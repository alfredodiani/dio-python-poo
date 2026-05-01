import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(conexao, cursor):
    cursor.execute("""
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100),
            email VARCHAR(150)
        )
        """)
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("""
        INSERT INTO clientes (nome, email)
        VALUES (?, ?);
    """, data)

    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("""
        UPDATE clientes
        SET nome = ?, email = ?
        WHERE id = ?;
    """, data)
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("""
        DELETE FROM clientes
        WHERE id = ?;
    """, data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("""
        INSERT INTO clientes (nome, email)
        VALUES (?,?);
    """, dados)
    conexao.commit()

def recuperar_cliente(cursor, id):
    
    cursor.execute("SELECT * FROM clientes WHERE id = ?;", (id,))
    resultado = cursor.fetchone()
    return resultado

def listar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes;")
    resultado = cursor.fetchall()
    return resultado

# inserir_registro(conexao, cursor, "James None", "jnone@email.com")

# atualizar_registro(conexao, cursor, "John Doe", "johndoe@email.com", 1)
# atualizar_registro(conexao, cursor, "Jane Doe", "janedoe@email.com", 2)

# excluir_registro(conexao, cursor, 2)

# dados = [
#     ("JJ", "jj@email.com"),
#     ("KK", "kk@email.com"),
#     ("LL", "ll@email.com"),
#     ("MM", "mm@email.com"),
# ]
# inserir_muitos(conexao, cursor, dados)



clientes = listar_clientes(cursor)
for c in clientes:
    print(dict(c))

cliente = recuperar_cliente(cursor, 1)
print(cliente["id"], cliente["nome"])
print(dict(cliente))
print(cliente["id"], cliente["nome"])