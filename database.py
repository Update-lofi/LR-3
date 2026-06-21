import sqlite3
from datetime import datetime

DATABASE_NAME = 'diary.db'


def get_db_connection():
    """Устанавливает соединение с БД, возвращает объект соединения"""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # Позволяет обращаться к полям по имени
    return conn


def init_db():
    """Создаёт таблицу entries, если её нет"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at DATE NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()


def add_entry(title, content):
    """Добавляет новую запись (дата ставится автоматически)"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Получаем текущую дату и время
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
        INSERT INTO entries (title, content, created_at)
        VALUES (?, ?, ?)
    ''', (title, content, current_date))
    
    conn.commit()
    conn.close()


def get_all_entries():
    """Возвращает все записи, отсортированные от новых к старым"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM entries
        ORDER BY created_at DESC
    ''')
    
    entries = cursor.fetchall()
    conn.close()
    
    return entries


def get_entry(entry_id):
    """Возвращает одну запись по id"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM entries
        WHERE id = ?
    ''', (entry_id,))
    
    entry = cursor.fetchone()
    conn.close()
    
    return entry


def update_entry(entry_id, title, content):
    """Обновляет заголовок и текст записи"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE entries
        SET title = ?, content = ?
        WHERE id = ?
    ''', (title, content, entry_id))
    
    conn.commit()
    conn.close()


def delete_entry(entry_id):
    """Удаляет запись по id"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        DELETE FROM entries
        WHERE id = ?
    ''', (entry_id,))

def get_entries_count():
    """Возвращает количество записей"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM entries')
    count = cursor.fetchone()[0]
    
    conn.close()
    return count


def search_entries(query):
    """Ищет записи, где заголовок содержит query"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM entries
        WHERE title LIKE ?
    ''', (f'%{query}%',))
    
    entries = cursor.fetchall()
    conn.close()
    
    return entries


def delete_all_entries():
    """Удаляет все записи"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM entries')
    
    conn.commit()
    conn.close()


def get_last_week_entries():
    """Возвращает записи за последние 7 дней"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT * FROM entries
        WHERE created_at >= datetime('now', '-7 days')
        ORDER BY created_at DESC
    ''')
    
    entries = cursor.fetchall()
    conn.close()
    
    return entries
    
    conn.commit()
    conn.close()