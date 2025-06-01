import sqlite3

class DatabaseManager:
    def __init__(self, db_name="transcriber.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS transcriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            transcription TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_transcription(self, filename, transcription):
        query = "INSERT INTO transcriptions (filename, transcription) VALUES (?, ?);"
        self.conn.execute(query, (filename, transcription))
        self.conn.commit()

    def update_transcription(self, transcription_id, new_text):
        query = "UPDATE transcriptions SET transcription = ? WHERE id = ?;"
        self.conn.execute(query, (new_text, transcription_id))
        self.conn.commit()

    def delete_transcription(self, transcription_id):
        query = "DELETE FROM transcriptions WHERE id = ?;"
        self.conn.execute(query, (transcription_id,))
        self.conn.commit()

    def get_all_transcriptions(self):
        cursor = self.conn.execute("SELECT * FROM transcriptions;")
        return cursor.fetchall()

    def close(self):
        self.conn.close()
