import mysql.connector

#MySQL 연결 설정
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="251015_test"
)

# 커서 생성
cursor = conn.cursor()

# 테이블 생성 (예시)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100)
)
""")

# 데이터 삽입 (Create)
sql_insert = "INSERT INTO users (name, email) VALUES (%s, %s)"
values = ("홍길동", "hong@example.com")
cursor.execute(sql_insert, values)
conn.commit()
print("✅ 데이터 삽입 완료")

# 데이터 조회 (Read)
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

# 데이터 수정 (Update)
sql_update = "UPDATE users SET email = %s WHERE name = %s"
cursor.execute(sql_update, ("hong123@example.com", "홍길동"))
conn.commit()
print("✅ 데이터 수정 완료")

# 데이터 삭제 (Delete)
sql_delete = "DELETE FROM users WHERE name = %s"
cursor.execute(sql_delete, ("홍길동",))
conn.commit()
print("✅ 데이터 삭제 완료")

# 연결 종료
cursor.close()
conn.close()