import sqlite3
conn = sqlite3.connect("law_firm.db")
cursor = conn.cursor()
# Сыртқы кілттерді қосу
cursor.execute("PRAGMA foreign_keys = ON")
# 1. Кестелерді құру
cursor.executescript("""
CREATE TABLE IF NOT EXISTS Clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    address TEXT,
    client_type TEXT
);

CREATE TABLE IF NOT EXISTS Lawyers (
    lawyer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    specialization TEXT,
    category TEXT,
    experience_years INTEGER,
    phone TEXT
);

CREATE TABLE IF NOT EXISTS Cases (
    case_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    lawyer_id INTEGER NOT NULL,
    case_title TEXT NOT NULL,
    case_type TEXT,
    start_date TEXT,
    status TEXT,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id),
    FOREIGN KEY (lawyer_id) REFERENCES Lawyers(lawyer_id)
);

CREATE TABLE IF NOT EXISTS Payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER NOT NULL,
    amount NUMERIC(10,2),
    payment_date TEXT,
    payment_method TEXT,
    payment_status TEXT,
    FOREIGN KEY (case_id) REFERENCES Cases(case_id)
);
""")

# 2. Clients кестесі: 10 клиент
clients = [
    ("Айдана Сәрсенова", "87011111111", "aidana@mail.kz", "Астана", "Жеке тұлға"),
    ("Ерлан Мұратов", "87022222222", "yerlan@mail.kz", "Алматы", "Жеке тұлға"),
    ("ABC Company", "87033333333", "abc@mail.kz", "Астана", "Заңды тұлға"),
    ("Дана Қасымова", "87044444444", "dana@mail.kz", "Қарағанды", "Жеке тұлға"),
    ("Нұрлан Әбілов", "87055555555", "nurlan@mail.kz", "Шымкент", "Жеке тұлға"),
    ("Global Trade LLP", "87066666666", "global@mail.kz", "Алматы", "Заңды тұлға"),
    ("Мадина Омарова", "87077777777", "madina@mail.kz", "Астана", "Жеке тұлға"),
    ("Арман Төлеген", "87088888888", "arman@mail.kz", "Ақтөбе", "Жеке тұлға"),
    ("Berkut Group", "87099999999", "berkut@mail.kz", "Атырау", "Заңды тұлға"),
    ("Әлия Жұмабек", "87000000000", "aliya@mail.kz", "Өскемен", "Жеке тұлға")
]

cursor.executemany("""
INSERT INTO Clients
(full_name, phone, email, address, client_type)
VALUES (?, ?, ?, ?, ?)
""", clients)

# 3. Lawyers кестесі: 10 адвокат
lawyers = [
    ("Алихан Нұрланов", "Азаматтық құқық", "Жоғары", 10, "87110000001"),
    ("Дана Қасымова", "Қылмыстық құқық", "Бірінші", 7, "87110000002"),
    ("Марат Сейітов", "Еңбек құқығы", "Жоғары", 12, "87110000003"),
    ("Аружан Бекова", "Отбасы құқығы", "Екінші", 5, "87110000004"),
    ("Ермек Жанұзақ", "Салық құқығы", "Бірінші", 8, "87110000005"),
    ("Айгерім Нұржан", "Азаматтық құқық", "Екінші", 4, "87110000006"),
    ("Самат Қожахмет", "Әкімшілік құқық", "Жоғары", 15, "87110000007"),
    ("Жанар Әлиева", "Қылмыстық құқық", "Бірінші", 9, "87110000008"),
    ("Руслан Мұхтар", "Кәсіпкерлік құқық", "Жоғары", 11, "87110000009"),
    ("Алина Сапарова", "Еңбек құқығы", "Екінші", 3, "87110000010")
]

cursor.executemany("""
INSERT INTO Lawyers
(full_name, specialization, category, experience_years, phone)
VALUES (?, ?, ?, ?, ?)
""", lawyers)

# 4. Cases кестесі: 10 іс
cases = [
    (1, 1, "Мүлік дауы", "Азаматтық", "2026-01-10", "Қаралуда"),
    (2, 2, "Қылмыстық іс", "Қылмыстық", "2026-01-15", "Ашық"),
    (3, 3, "Келісімшарт дауы", "Азаматтық", "2026-01-20", "Жабық"),
    (4, 4, "Алимент өндіру", "Азаматтық", "2026-02-01", "Қаралуда"),
    (5, 5, "Еңбек дауы", "Еңбек", "2026-02-05", "Ашық"),
    (6, 6, "Салық мәселесі", "Әкімшілік", "2026-02-10", "Қаралуда"),
    (7, 7, "Мұрагерлік дауы", "Азаматтық", "2026-02-15", "Жабық"),
    (8, 8, "Шарт талаптарын бұзу", "Азаматтық", "2026-03-01", "Ашық"),
    (9, 9, "Компания мүддесін қорғау", "Азаматтық", "2026-03-05", "Қаралуда"),
    (10, 10, "Жұмысқа қайта орналастыру", "Еңбек", "2026-03-10", "Ашық")
]

cursor.executemany("""
INSERT INTO Cases
(client_id, lawyer_id, case_title, case_type, start_date, status)
VALUES (?, ?, ?, ?, ?, ?)
""", cases)

# 5. Payments кестесі: 10 төлем
payments = [
    (1, 150000, "2026-01-12", "Карта", "Төленді"),
    (1, 50000, "2026-01-25", "Аударым", "Төленді"),
    (2, 200000, "2026-01-18", "Қолма-қол", "Күтілуде"),
    (3, 100000, "2026-01-22", "Карта", "Төленді"),
    (4, 75000, "2026-02-03", "Аударым", "Төленді"),
    (5, 120000, "2026-02-07", "Карта", "Күтілуде"),
    (6, 90000, "2026-02-12", "Қолма-қол", "Төленді"),
    (7, 180000, "2026-02-17", "Аударым", "Төленді"),
    (8, 65000, "2026-03-03", "Карта", "Күтілуде"),
    (10, 110000, "2026-03-12", "Аударым", "Төленді")
]

cursor.executemany("""
INSERT INTO Payments
(case_id, amount, payment_date, payment_method, payment_status)
VALUES (?, ?, ?, ?, ?)
""", payments)

conn.commit()
conn.close()
print("\nБағдарлама сәтті аяқталды!")

