import psycopg2
from psycopg2 import sql

try:
    conn = psycopg2.connect(host="85.192.35.124", port=5432, user="manuscript_2024", password="manuscript_ban_24", database="dbstud")
    cur = conn.cursor()
    insert_query = sql.SQL("INSERT INTO test (id) VALUES (%s)")
    cur.execute(insert_query, (2,))  
    conn.commit()
    cur.close()
    conn.close()
    print(f"Строка вставлена успешно")
except psycopg2.Error as e:
    print(f"Ошибка при вставки в базу данных: {e}")