import sqlite3

def connect():
    conn = sqlite3.connect('laptops')
    conn.execute("CREATE TABLE IF NOT EXISTS LAPTOPS (NAME TEXT, PRICE TEXT, RATING TEXT, DISCOUNT TEXT, FEATURES TEXT)")
    print("Table created successfully")
    conn.close()

def insert_into_table(values):
    conn = sqlite3.connect('laptops')
    insert_sql = "INSERT INTO LAPTOPS (NAME, PRICE, RATING, DISCOUNT, FEATURES) VALUES(?,?,?,?,?)"
    conn.execute(insert_sql, values)
    conn.commit()
    conn.close()

def get_laptop_info():
    conn = sqlite3.connect('laptops')
    cur = conn.cursor()
    cur.execute("SELECT * FROM LAPTOPS")
    table_data = cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()



