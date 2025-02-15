import psycopg2

def get_db_stuff():
    conn = psycopg2.connect(database="postgres",
                            host="127.0.0.1",
                            user="postgres",
                            password="mysecretpassword",
                            port="5432")
    cur = conn.cursor()
    cur.execute("SELECT * FROM DB_table WHERE name = 'Alice'")
    rows = cur.fetchall()
    names = []
    for row in rows:
        names.append(row[0])

    return names