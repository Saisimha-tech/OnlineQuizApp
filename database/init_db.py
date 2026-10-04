import sqlite3
import os

# Find the main OnlineQuizApp folder
base_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create the path for quiz.db
database_path = os.path.join(base_folder, "quiz.db")

# Connect to SQLite database
connection = sqlite3.connect(database_path)

cursor = connection.cursor()

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# Questions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS questions (
    question_id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL,
    category TEXT
)
""")

# Results table
cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    total_questions INTEGER NOT NULL,
    attempt_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""")
# Insert quiz questions
questions = [
    (
        "What does HTML stand for?",
        "Hyper Text Markup Language",
        "High Text Machine Language",
        "Hyperlinks Text Management Language",
        "Home Tool Markup Language",
        "A",
        "Web Development"
    ),
    (
        "Which language is used to style web pages?",
        "Python",
        "CSS",
        "SQL",
        "C",
        "B",
        "Web Development"
    ),
    (
        "Which language adds interactivity to a webpage?",
        "HTML",
        "SQL",
        "JavaScript",
        "CSS",
        "C",
        "Web Development"
    ),
    (
        "Which one is a database?",
        "HTML",
        "CSS",
        "SQLite",
        "Windows",
        "C",
        "Database"
    ),
    (
        "Which keyword declares a variable in JavaScript?",
        "let",
        "print",
        "echo",
        "define",
        "A",
        "JavaScript"
    )
]

cursor.executemany("""
INSERT INTO questions
(question_text, option_a, option_b, option_c, option_d, correct_answer, category)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", questions)
connection.commit()
connection.close()

print("Database and all tables created successfully!")
print("Database location:", database_path)