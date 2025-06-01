import sqlite3

def conectar_banco():
    return sqlite3.connect("transcriber.db")

def criar_tabelas():
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transcriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            transcription TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    conn.close()

def inserir_transcricao(filename, texto):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transcriptions (filename, transcription)
        VALUES (?, ?);
    """, (filename, texto))

    conn.commit()
    conn.close()

def atualizar_transcricao(id, novo_texto):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE transcriptions
        SET transcription = ?
        WHERE id = ?;
    """, (novo_texto, id))

    conn.commit()
    conn.close()


def remover_transcricao(id):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transcriptions WHERE id = ?;", (id,))
    conn.commit()
    conn.close()
