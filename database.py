import os
import psycopg2
from psycopg2 import sql
from config import MANHWA_LIST

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set. Please add it to environment variables.")

def get_connection():
    return psycopg2.connect(DATABASE_URL, sslmode="require")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # جدول المستخدمين
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id BIGINT PRIMARY KEY,
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
    cursor.close()
    conn.close()

def add_user(user_id, username, first_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (user_id, username, first_name)
        VALUES (%s, %s, %s)
        ON CONFLICT (user_id)
        DO UPDATE SET username = EXCLUDED.username, first_name = EXCLUDED.first_name
    """, (user_id, username, first_name))
    conn.commit()
    cursor.close()
    conn.close()

def update_view(key):
    if key not in MANHWA_LIST:
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO manhwa_stats (key) VALUES (%s) ON CONFLICT (key) DO NOTHING", (key,))
    cursor.execute("UPDATE manhwa_stats SET views = views + 1 WHERE key = %s", (key,))
    conn.commit()
    cursor.close()
    conn.close()

def update_like(key):
    if key not in MANHWA_LIST:
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO manhwa_stats (key) VALUES (%s) ON CONFLICT (key) DO NOTHING", (key,))
    cursor.execute("UPDATE manhwa_stats SET likes = likes + 1 WHERE key = %s", (key,))
    conn.commit()
    cursor.close()
    conn.close()

def update_share(key):
    if key not in MANHWA_LIST:
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO manhwa_stats (key) VALUES (%s) ON CONFLICT (key) DO NOTHING", (key,))
    cursor.execute("UPDATE manhwa_stats SET shares = shares + 1 WHERE key = %s", (key,))
    conn.commit()
    cursor.close()
    conn.close()

def get_stats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    cursor.execute("SELECT key, views, likes, shares FROM manhwa_stats")
    manhwa_data = cursor.fetchall()

    cursor.close()
    conn.close()
    return total_users, manhwa_data
