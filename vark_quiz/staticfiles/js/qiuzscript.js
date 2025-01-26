document.addEventListener('DOMContentLoaded', function() {
    const startBtn = document.querySelector('.play-now');
    const popupInfo = document.querySelector('.popup_info');
    const exitBtn = document.querySelector('.exit_btn');
    const main = document.querySelector('.main');
    const continueBtn = document.querySelector('.continue-btn');
    const quizSection = document.querySelector('.quiz-section');
    const quizBtn = document.querySelector('.quiz-box');
    const isAuthenticated = JSON.parse(document.getElementById('isAuthenticated').textContent);

    if (startBtn) {
        startBtn.addEventListener('click', function() {
            popupInfo.classList.add('active');
            main.classList.add('active');
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
                quizSection.classList.add('active');
                popupInfo.classList.remove('active');
                main.classList.remove('active');
                quizBtn.classList.add('active');
            } else {
                alert('You need to log in to continue the quiz.');
                window.location.href = '/accounts/login/';
            }
        });
    }
});