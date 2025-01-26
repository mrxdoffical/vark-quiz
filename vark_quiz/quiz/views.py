from django.shortcuts import render, get_object_or_404
from .models import Question, Answer, QuizResult, AggregatedQuizResult
from tips.models import Tip
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

@login_required
def quiz_home(request):
    questions = Question.objects.all()
    return render(request, 'quiz/home.html', {'questions': questions})

@login_required
def quiz_question(request):
    questions = list(Question.objects.all())
    if not questions:
        return JsonResponse({'error': 'No questions available'}, status=400)

    if request.method == 'GET':
        questions_data = []
        for question in questions:
            answers = Answer.objects.filter(question=question)
            questions_data.append({
                'id': question.id,
                'text': question.text,
                'answers': [{'id': answer.id, 'text': answer.text, 'letter': answer.letter, 'is_correct': answer.is_correct} for answer in answers]
            })
        return JsonResponse({'questions': questions_data})

    if request.method == 'POST':
        data = json.loads(request.body)
        question_id = data.get('question_id')
        selected_ans_id = data.get('selected_ans_id')
        if question_id and selected_ans_id:
            question = get_object_or_404(Question, id=question_id)
            answer = get_object_or_404(Answer, id=selected_ans_id)
            QuizResult.objects.create(
                user=request.user,
                question=question,
                answer=answer,
                is_correct=answer.is_correct
            )
        return JsonResponse({'success': True})

@login_required
def quiz_result(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        learning_patterns = data['learningPatterns']
        current_quiz_results = data['currentQuizResults']
        learning_patterns = {k: int(v) if v is not None else 0 for k, v in learning_patterns.items()}
        results_data = {
            'total_questions': sum(learning_patterns.values()),
            'visual': learning_patterns.get('V', 0),
            'auditory': learning_patterns.get('A', 0),
            'reading_writing': learning_patterns.get('R', 0),
            'kinesthetic': learning_patterns.get('K', 0),
            'current_quiz_results': current_quiz_results
        }
        AggregatedQuizResult.objects.create(
            user=request.user,
            total_questions=results_data['total_questions'],
            visual=results_data['visual'],
            auditory=results_data['auditory'],
            reading_writing=results_data['reading_writing'],
            kinesthetic=results_data['kinesthetic'],
            current_quiz_results=results_data['current_quiz_results']
        )

        # Determine the dominant learning pattern
        dominant_pattern = max(learning_patterns, key=learning_patterns.get)
        tip = Tip.objects.filter(learning_pattern__pattern=dominant_pattern).first()

        return render(request, 'quiz/result.html', {'results': results_data, 'tip': tip})
    
    elif request.method == 'GET':
        latest_results = AggregatedQuizResult.objects.filter(user=request.user).order_by('-id').first()
        if latest_results:
            results_data = {
                'total_questions': latest_results.total_questions,
                'visual': latest_results.visual,
                'auditory': latest_results.auditory,
                'reading_writing': latest_results.reading_writing,
                'kinesthetic': latest_results.kinesthetic,
                'current_quiz_results': latest_results.current_quiz_results
            }

            # Determine the dominant learning pattern
            learning_patterns = {
                'V': latest_results.visual,
                'A': latest_results.auditory,
                'R': latest_results.reading_writing,
                'K': latest_results.kinesthetic
            }
            dominant_pattern = max(learning_patterns, key=learning_patterns.get)
            tip = Tip.objects.filter(learning_pattern__pattern=dominant_pattern).first()

            return render(request, 'quiz/result.html', {'results': results_data, 'tip': tip})
        else:
            return render(request, 'quiz/result.html', {'error': 'No results available'}, status=400)
    
    else:
        return render(request, 'quiz/result.html', {'error': 'Invalid request method.', 'user': request.user})

def home(request):
    return render(request, 'quiz/home.html')

def about(request):
    return render(request, 'quiz/about.html')