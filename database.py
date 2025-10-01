import sqlite3
from config import MANHWA_LIST

DB_NAME = "users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # جدول المستخدمين
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            last_seen_manhwa TEXT,
            last_seen_chapter INTEGER,
            liked_manhwa TEXT,
            shared_count INTEGER DEFAULT 0
        )
    """)
    # جدول الإحصائيات لكل مانهوا
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS manhwa_stats (
            key TEXT PRIMARY KEY,
            views INTEGER DEFAULT 0,
            likes INTEGER DEFAULT 0,
            shares INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def add_user(user_id, username, first_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO users (user_id, username, first_name)
        VALUES (?, ?, ?)
    """, (user_id, username, first_name))
    conn.commit()
    conn.close()

def update_view(key):
    if key not in MANHWA_LIST:
        return
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO manhwa_stats (key) VALUES (?)", (key,))
    cursor.execute("UPDATE manhwa_stats SET views = views + 1 WHERE key = ?", (key,))
    conn.commit()
    conn.close()

def update_like(key):
    if key not in MANHWA_LIST:
        return
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO manhwa_stats (key) VALUES (?)", (key,))
    cursor.execute("UPDATE manhwa_stats SET likes = likes + 1 WHERE key = ?", (key,))
    conn.commit()
    conn.close()

def update_share(key):
    if key not in MANHWA_LIST:
        return
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO manhwa_stats (key) VALUES (?)", (key,))
    cursor.execute("UPDATE manhwa_stats SET shares = shares + 1 WHERE key = ?", (key,))
    conn.commit()
    conn.close()

def get_stats():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]
    cursor.execute("SELECT key, views, likes, shares FROM manhwa_stats")
    manhwa_data = cursor.fetchall()
    conn.close()
    return total_users, manhwa_data
