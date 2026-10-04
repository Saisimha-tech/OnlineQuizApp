const quizQuestions = questions.map(q => ({
    question: q.question_text,
    options: [
        q.option_a,
        q.option_b,
        q.option_c,
        q.option_d
    ],
    answer: ["A", "B", "C", "D"].indexOf(q.correct_answer)
}));

let currentQuestion = 0;
let score = 0;
let selectedAnswer = null;

const questionElement = document.getElementById("question");
const optionsElement = document.getElementById("options");
const progressElement = document.getElementById("progress");
const nextButton = document.getElementById("next-btn");

function showQuestion() {
    selectedAnswer = null;

    const q = quizQuestions[currentQuestion];

    progressElement.textContent =
        `Question ${currentQuestion + 1} of ${quizQuestions.length}`;

    questionElement.textContent = q.question;
    optionsElement.innerHTML = "";

    q.options.forEach((option, index) => {
        const button = document.createElement("button");

        button.textContent = option;
        button.className = "option";

        button.addEventListener("click", () => {
            selectedAnswer = index;

            document.querySelectorAll(".option").forEach(btn => {
                btn.classList.remove("selected");
            });

            button.classList.add("selected");
        });

        optionsElement.appendChild(button);
    });

    nextButton.disabled = false;

    nextButton.textContent =
        currentQuestion === quizQuestions.length - 1
            ? "Submit Quiz"
            : "Next Question";
}

nextButton.addEventListener("click", () => {
    if (selectedAnswer === null) {
        alert("Please select an answer!");
        return;
    }

    if (selectedAnswer === quizQuestions[currentQuestion].answer) {
        score++;
    }

    currentQuestion++;

    if (currentQuestion < quizQuestions.length) {
        showQuestion();
    } else {
        showResult();
    }
});

function showResult() {
    document.getElementById("quiz").classList.add("hidden");
    document.getElementById("result").classList.remove("hidden");

    document.getElementById("score").textContent =
        `You scored ${score} out of ${quizQuestions.length}!`;
}

function restartQuiz() {
    currentQuestion = 0;
    score = 0;

    document.getElementById("quiz").classList.remove("hidden");
    document.getElementById("result").classList.add("hidden");

    showQuestion();
}

showQuestion();