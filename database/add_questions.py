import sqlite3
import os

# Find the main project folder
base_folder = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Use the SAME database used by app.py
database_path = os.path.join(base_folder, "quiz.db")

connection = sqlite3.connect(database_path)

questions = [

    (
        "Which keyword is used to define a function in Python?",
        "func",
        "def",
        "function",
        "define",
        "B",
        "Python"
    ),

    (
        "Which data structure follows LIFO?",
        "Queue",
        "Array",
        "Stack",
        "Linked List",
        "C",
        "Data Structures"
    ),

    (
        "Which SQL command is used to retrieve data?",
        "INSERT",
        "UPDATE",
        "SELECT",
        "DELETE",
        "C",
        "Database"
    ),

    (
        "Which operating system manages computer hardware and software resources?",
        "Compiler",
        "Operating System",
        "Browser",
        "Database",
        "B",
        "Operating Systems"
    ),

    (
        "Which protocol is commonly used to access web pages?",
        "FTP",
        "HTTP",
        "SMTP",
        "SSH",
        "B",
        "Computer Networks"
    ),

    (
        "Which of the following is NOT a programming language?",
        "Python",
        "Java",
        "HTML",
        "C++",
        "C",
        "Programming"
    ),

    (
        "What does CPU stand for?",
        "Central Processing Unit",
        "Computer Processing Unit",
        "Central Program Unit",
        "Computer Program Utility",
        "A",
        "Computer Fundamentals"
    ),

    (
        "Which data structure uses FIFO principle?",
        "Stack",
        "Queue",
        "Tree",
        "Graph",
        "B",
        "Data Structures"
    ),

    (
        "Which SQL command is used to add new data to a table?",
        "INSERT",
        "ADD",
        "CREATE",
        "APPEND",
        "A",
        "Database"
    ),

    (
        "Which device is used to connect different networks?",
        "Switch",
        "Router",
        "Keyboard",
        "Monitor",
        "B",
        "Computer Networks"
    )

]

connection.executemany(
    """
    INSERT INTO questions
    (
        question_text,
        option_a,
        option_b,
        option_c,
        option_d,
        correct_answer,
        category
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    questions
)

connection.commit()

# Verify the total
total = connection.execute(
    "SELECT COUNT(*) FROM questions"
).fetchone()[0]

connection.close()

print("10 new questions added successfully!")
print("Total questions now:", total)