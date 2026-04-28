import sqlite3
import os

# 確保 instance 資料夾存在並設定正確的 DB 檔案路徑
DB_DIR = 'instance'
DATABASE = os.path.join(DB_DIR, 'database.db')

if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

class NoteModel:
    @staticmethod
    def create(title, content, rating):
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO notes (title, content, rating) VALUES (?, ?, ?)',
            (title, content, rating)
        )
        conn.commit()
        conn.close()
        
    @staticmethod
    def get_all():
        conn = get_db_connection()
        notes = conn.execute('SELECT * FROM notes ORDER BY created_at DESC').fetchall()
        conn.close()
        return [dict(note) for note in notes]

    @staticmethod
    def search(keyword):
        conn = get_db_connection()
        search_kw = f"%{keyword}%"
        notes = conn.execute(
            'SELECT * FROM notes WHERE title LIKE ? OR content LIKE ? ORDER BY created_at DESC',
            (search_kw, search_kw)
        ).fetchall()
        conn.close()
        return [dict(note) for note in notes]

    @staticmethod
    def get_by_id(note_id):
        conn = get_db_connection()
        note = conn.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()
        conn.close()
        return dict(note) if note else None

    @staticmethod
    def update(note_id, title, content, rating):
        conn = get_db_connection()
        conn.execute(
            'UPDATE notes SET title = ?, content = ?, rating = ? WHERE id = ?',
            (title, content, rating, note_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(note_id):
        conn = get_db_connection()
        conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
        conn.commit()
        conn.close()
