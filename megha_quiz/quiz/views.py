from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Question

def home_page(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

@login_required
def quiz_view(request):
    if request.method == "POST":
        score = 0
        for key, value in request.POST.iteritems():
            if 'option' in key:
                question = Question.objects.get(id=key.split('_')[1])
                if question.correct_answer == int(value):
                    score += 1
        return render(request, 'score.html', {'score': score})
    
    questions = Question.objects.all()
    return render(request, 'quiz.html', {'questions': questions})