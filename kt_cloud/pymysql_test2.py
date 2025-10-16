import pymysql

# MySQL 연결 설정
conn = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="251015_test",        # 사용할 데이터베이스
    port=3306,                 # 기본 포트 (3306)
    charset="utf8mb4",         # UTF-8 인코딩
    cursorclass=pymysql.cursors.DictCursor  # 결과를 dict 형태로 반환
)

# 커서 생성
cursor = conn.cursor()

# 🧱 테이블 생성 (존재하지 않으면)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100)
)
""")
print("✅ 테이블 확인 완료")

# ➕ 데이터 삽입 (Create)
sql_insert = "INSERT INTO users (name, email) VALUES (%s, %s)"
cursor.execute(sql_insert, ("홍길동", "hong@example.com"))
conn.commit()
print("✅ 데이터 삽입 완료")

# 🔍 데이터 조회 (Read)
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("📋 전체 사용자 목록:")
for row in rows:
    print(row)

# ✏️ 데이터 수정 (Update)
sql_update = "UPDATE users SET email = %s WHERE name = %s"
cursor.execute(sql_update, ("hong_new@example.com", "홍길동"))
conn.commit()
print("✅ 데이터 수정 완료")

# ❌ 데이터 삭제 (Delete)
sql_delete = "DELETE FROM users WHERE name = %s"
cursor.execute(sql_delete, ("홍길동",))
conn.commit()
print("✅ 데이터 삭제 완료")

# 연결 종료
cursor.close()
conn.close()
