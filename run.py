import os
import sqlite3
from flask import Flask
from app.routes.note_routes import note_bp

def create_app():
    app = Flask(__name__)
    # 設定一個隨機的 SECRET_KEY 以供 session 與 flash messages 使用
    app.config['SECRET_KEY'] = 'dev-secret-key-12345'
    
    # 註冊 blueprint
    app.register_blueprint(note_bp)
    
    return app

def init_db():
    if not os.path.exists('instance'):
        os.makedirs('instance')
    
    with open('database/schema.sql', 'r', encoding='utf-8') as f:
        schema = f.read()
        
    conn = sqlite3.connect('instance/database.db')
    conn.executescript(schema)
    conn.commit()
    conn.close()
    print("Database initialized.")

app = create_app()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
