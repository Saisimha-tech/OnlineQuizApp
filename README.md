# 🧠 Online Quiz Application

A web-based Online Quiz Application developed as a BCA project using Flask, Python, HTML, CSS, JavaScript, and SQLite.

The application allows users to create an account, log in, take a timed quiz, view their scores, and track their previous quiz attempts.

## ✨ Features

* User registration and login
* Secure password hashing
* SQLite database integration
* 15 quiz questions
* Multiple-choice questions
* Questions organized by category
* Randomized question order
* One-question-at-a-time quiz interface
* Next and Previous navigation
* Quiz progress bar
* 10-minute countdown timer
* Answer validation
* Automatic score calculation
* Percentage calculation
* Best score tracking
* Average score tracking
* Attempt history
* Responsive user interface

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **JavaScript**
* **SQLite**
* **Jinja2**
* **Werkzeug**

## 📁 Project Structure

```text
OnlineQuizApp/
│
├── app.py
├── quiz.db
├── requirements.txt
├── README.md
│
├── database/
│   ├── init_db.py
│   └── add_questions.py
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    ├── login.html
    ├── register.html
    ├── quiz.html
    └── results.html
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Saisimha-tech/OnlineQuizApp.git
```

### 2. Open the project folder

```bash
cd OnlineQuizApp
```

### 3. Install the required package

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open the application

Open the following address in your browser:

```text
http://127.0.0.1:5000/
```

## 🎯 Quiz Categories

The application currently contains questions from areas such as:

* Web Development
* Python
* Database
* Data Structures
* Operating Systems
* Computer Networks
* Programming
* Computer Fundamentals

## 🔮 Future Improvements

* Admin panel for adding and managing questions
* More quiz categories
* Larger question bank
* Difficulty levels
* User profile page
* Leaderboard
* Online deployment
* Improved security and authentication
* Mobile-friendly enhancements

## 📌 Project Purpose

This project was developed as a practical BCA project to demonstrate skills in web development, Python programming, Flask, database management, JavaScript, and user authentication.

## 📄 License

This project is created for educational and portfolio purposes.
