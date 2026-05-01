import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?)', ('teste1', 'teste@email.com'))
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?,?,?)', (2, 'teste1', 'teste@email.com'))
    conexao.commit()
except Exception as e:
    print(f'Ocorreu um erro! {e}')
    conexao.rollback()