import sqlite3

DB = "event_system.db"

def get_connection():
    conn = sqlite3.connect(DB, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor() 

    # USERS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)


    # VENUES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS venues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        capacity INTEGER
    )
    """)

    # EVENTS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        type TEXT,
        date TEXT,
        venue TEXT,
        planned_budget REAL,
        created_by TEXT
    )
    """)

    # EXPENSES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_id INTEGER,
        vendor TEXT,
        amount REAL
    )
    """)

    # PARTICIPANTS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS participants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_id INTEGER,
        name TEXT,
        attended INTEGER DEFAULT 0
    )
    """)

    # FEEDBACK
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_id INTEGER,
        comment TEXT,
        rating INTEGER
    )
    """)

    # STAFF
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS staff (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        role TEXT,
        phone TEXT
    )
    """)

    # STAFF ASSIGNMENTS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS staff_assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_id INTEGER,
        staff_id INTEGER,
        duty TEXT
    )
    """)

    # RESOURCES
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        quantity INTEGER,
        staff_role TEXT
    )
    """)

    # RESOURCE REQUESTS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resource_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_id INTEGER,
        requested_by TEXT,
        resource_name TEXT,
        quantity INTEGER,
        status TEXT DEFAULT 'Pending'
    )
    """)

    # Add Pune venues if empty
    cursor.execute("SELECT COUNT(*) FROM venues")
    if cursor.fetchone()[0] == 0:
        venues = [
            ("Balewadi Stadium Convention Hall", 2000),
            ("MIT World Peace University Auditorium", 1500),
            ("Symbiosis Auditorium Lavale", 1000),
            ("JW Marriott Pune Conference Hall", 500),
            ("The Orchid Hotel Pune Banquet Hall", 400)
        ]
        for v in venues:
            cursor.execute("INSERT INTO venues (name,capacity) VALUES (?,?)", v)

    conn.commit()
    conn.close()
