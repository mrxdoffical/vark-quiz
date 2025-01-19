# vark_quiz/quiz/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer, QuizResult
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def quiz_home(request):
    questions = Question.objects.all()
    return render(request, 'templates/quiz/home.html', {'questions': questions})

@login_required
def quiz_question(request, question_id):
    questions = Question.objects.all()
    if request.method == 'POST':
        result = {'v': 0, 'a': 0, 'r': 0, 'k': 0}
        for question in questions:
            selected_ans_id = request.POST.get(f'question_{question.id}')
            if selected_ans_id:
                answer = Answer.objects.get(id=selected_ans_id)
                result[answer.letter.lower()] += 1
                QuizResult.objects.create(
                    user=request.user,
                    question=question,
                    answer=answer,
                    is_correct=answer.is_correct
                )
        return JsonResponse(result)
    return render(request, 'quiz/question.html', {'questions': questions})

@login_required
def quiz_result(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    result = QuizResult.objects.filter(user=request.user, question=question).last()
    return render(request, 'quiz/result.html', {'result': result})