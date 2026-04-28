import os
import sqlite3
from flask import Flask

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

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key-12345'
    
    from app.routes.note_routes import note_bp
    app.register_blueprint(note_bp)
    
    return app
