document.addEventListener('DOMContentLoaded', function() {
    const quizContainer = document.getElementById('quiz-content');
    const startQuizBtn = document.querySelector('.play-now');
    const popupInfo = document.querySelector('.popup_info');
    const exitBtn = document.querySelector('.exit_btn');
    const continueBtn = document.querySelector('.continue-btn');
    const nextBtn = document.getElementById('next-btn'); // Use id for easier control
    const main = document.querySelector('.main');
    const isAuthenticated = JSON.parse(document.getElementById('isAuthenticated').textContent);
    let currentQuestionIndex = 0;
    let questions = [];
    let learningPatterns = { 'V': 0, 'A': 0, 'R': 0, 'K': 0 };
    let currentQuizResults = [];

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    if (startQuizBtn) {
        startQuizBtn.addEventListener('click', function() {
            popupInfo.classList.add('active');
            main.classList.add('active');
            fetchQuestions();
        });
    }

    if (exitBtn) {
        exitBtn.addEventListener('click', function() {
            popupInfo.classList.remove('active');
            main.classList.remove('active');
        });
    }

    if (continueBtn) {
        continueBtn.addEventListener('click', function() {
            if (isAuthenticated) {
                popupInfo.classList.remove('active');
                main.classList.remove('active');
                renderQuestion();
            } else {
                alert('You need to log in to continue the quiz.');
                window.location.href = '/accounts/login/';
            }
        });
    }

    function fetchQuestions() {
        fetch("/quiz/question/", {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            }
        })
        .then(response => response.json())
        .then(data => {
            console.log('Fetched questions:', data); // Debugging line
            if (data.error) {
                alert(data.error);
                return;
            }
            questions = data.questions;
            renderQuestion();
        });
    }

    function renderQuestion() {
        if (currentQuestionIndex >= questions.length) {
            console.log('Sending data to server:', { learningPatterns, currentQuizResults }); // Debugging line
            fetch("/quiz/results/", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ learningPatterns, currentQuizResults })
            })
            .then(response => {
                if (response.ok) {
                    window.location.href = '/quiz/results/';
                } else {
                    console.error('Failed to submit quiz results');
                }
            });
            return;
        }

        const question = questions[currentQuestionIndex];
        const answers = question.answers;
        const isLastQuestion = currentQuestionIndex === questions.length - 1;

        quizContainer.innerHTML = `
          <h2>${question.text}</h2>
          <form id="quiz-form">
            ${answers.map(answer => `
              <div>
                <input type="radio" name="answer" value="${answer.id}" data-letter="${answer.letter}" data-correct="${answer.is_correct}" id="answer_${answer.id}">
                <label for="answer_${answer.id}">${answer.text}</label>
              </div>
            `).join('')}
          </form>
        `;

        nextBtn.textContent = isLastQuestion ? 'Submit' : 'Next';
        nextBtn.disabled = true;
        nextBtn.classList.remove('active');

        const quizForm = document.getElementById('quiz-form');
        quizForm.addEventListener('change', function() {
            nextBtn.disabled = false;
            nextBtn.classList.add('active');
        });
    }

    nextBtn.addEventListener('click', function(event) {
        event.preventDefault();
        const selectedAnswer = document.querySelector('input[name="answer"]:checked');
        if (selectedAnswer) {
            const answerLetter = selectedAnswer.getAttribute('data-letter');
            learningPatterns[answerLetter]++;
            currentQuizResults.push({
                question: questions[currentQuestionIndex].text,
                answer: selectedAnswer.nextElementSibling.textContent,
                is_correct: selectedAnswer.getAttribute('data-correct') === 'true',
                answer_type: answerLetter
            });
            console.log('Current Quiz Results:', currentQuizResults); // Debugging line
            currentQuestionIndex++;
            renderQuestion();
        } else {
            alert('Please select an answer.');
        }
    });
});