const startBtn = document.querySelector('.play-now');
const popupInfo = document.querySelector('.popup_info');
const exitBtn = document.querySelector('.exit_btn');
const main = document.querySelector('.main');
const continueBtn = document.querySelector('.continue-btn');
const qiuzsection = document.querySelector('.quiz-section');
const quizBtn = document.querySelector('.quiz-box');
startBtn.onclick = () => {
    popupInfo.classList.add('active');
    main.classList.add('active');
}
exitBtn.onclick = () => {
    popupInfo.classList.remove('active');
    main.classList.remove('active');
}
continueBtn.onclick = () => {
    qiuzsection.classList.add('active');
    popupInfo.classList.remove('active');
    main.classList.remove('active');
    quizBtn.classList.add('active');
}