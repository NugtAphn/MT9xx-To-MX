import oracledb


def connect():
    user = 'hr'
    password = 'hr'
    dsn = 'localhost:1521/orcl'
    conn = oracledb.connect(user=user, password=password, dsn=dsn)

    cursor = conn.cursor()
    sql = "SELECT * FROM employees"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()
