from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "quiz_secret_key"


# Connect to the database
def get_db_connection():
    connection = sqlite3.connect("quiz.db")
    connection.row_factory = sqlite3.Row
    return connection


# Home page
@app.route("/")
def home():

    if "user_id" in session:

        return render_template(
            "index.html",
            logged_in=True,
            user_name=session["user_name"]
        )

    return render_template(
        "index.html",
        logged_in=False
    )





# Register
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = generate_password_hash(password)

        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO users (name, email, hashed_password)
            VALUES (?, ?, ?)
            """,
            (name, email, password)
        )

        connection.commit()
        connection.close()

        return redirect("/login")

    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        connection = get_db_connection()

        user = connection.execute(
            """
            SELECT * FROM users
            WHERE email = ? AND password = ?
            """,
            (email, password)
        ).fetchone()

        connection.close()

        if user:
            session["user_id"] = user["user_id"]
            session["user_name"] = user["name"]

            return redirect("/quiz")

        else:
            return "Invalid email or password"

    return render_template("login.html")


# Quiz page
@app.route("/quiz")
def quiz():

    if "user_id" not in session:
        return redirect("/login")

    connection = get_db_connection()

    questions = connection.execute(
        "SELECT * FROM questions ORDER BY RANDOM()"
    ).fetchall()

    connection.close()

    return render_template(
        "quiz.html",
        questions=questions
    )


# Submit quiz
@app.route("/submit", methods=["POST"])
def submit():

    if "user_id" not in session:
        return redirect("/login")

    connection = get_db_connection()

    questions = connection.execute(
        "SELECT * FROM questions"
    ).fetchall()

    score = 0

    for question in questions:

        user_answer = request.form.get(
            f"question_{question['question_id']}"
        )

        if user_answer == question["correct_answer"]:
            score += 1

    total_questions = len(questions)

    user_id = session.get("user_id")

    connection.execute(
        """
        INSERT INTO results
        (user_id, score, total_questions)
        VALUES (?, ?, ?)
        """,
        (user_id, score, total_questions)
    )

    connection.commit()
    connection.close()

    return redirect("/results")


# Results
@app.route("/results")
def results():

    user_id = session.get("user_id")

    if not user_id:
        return redirect("/login")

    connection = get_db_connection()

    # Get all attempts
    results = connection.execute(
        """
        SELECT score, total_questions, attempt_date
        FROM results
        WHERE user_id = ?
        ORDER BY attempt_date DESC
        """,
        (user_id,)
    ).fetchall()

    # Get user name
    user = connection.execute(
        "SELECT name FROM users WHERE user_id = ?",
        (user_id,)
    ).fetchone()

    connection.close()

    # Calculate statistics
    total_attempts = len(results)

    if total_attempts > 0:

        best_score = max(
            result["score"]
            for result in results
        )

        total_percentage = sum(
            (result["score"] / result["total_questions"]) * 100
            for result in results
        )

        average_score = round(
            total_percentage / total_attempts,
            1
        )

    else:

        best_score = 0
        average_score = 0

    return render_template(
        "results.html",
        results=[
            {
                **dict(result),
                "percentage": round(
                    (result["score"] / result["total_questions"]) * 100,
                    1
                )
            }
            for result in results
        ],
        user_name=user["name"],
        best_score=best_score,
        average_score=average_score,
        total_attempts=total_attempts,
        total_questions=results[0]["total_questions"]
        if results else 0
    )


# Logout
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# Start application
if __name__ == "__main__":
    app.run(debug=True)