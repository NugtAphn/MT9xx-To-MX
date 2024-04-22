import oracledb


def connect():
    user = 'tung'
    password = 'tung'
    dsn = 'localhost:1521/orcl'
    conn = oracledb.connect(user=user, password=password, dsn=dsn)

    cursor = conn.cursor()
    sql = "SELECT Bank_Name FROM BIC"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()
