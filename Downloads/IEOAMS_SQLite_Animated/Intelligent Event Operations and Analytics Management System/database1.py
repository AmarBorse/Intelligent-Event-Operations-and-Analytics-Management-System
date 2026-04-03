import sqlite3, hashlib
conn = sqlite3.connect("event_system.db")
conn.execute(
    "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
    ("admin", hashlib.sha256("admin123".encode()).hexdigest(), "Admin")
)
conn.commit()
conn.close()
print("Admin created successfully")