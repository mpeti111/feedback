from django.shortcuts import render, redirect
from .forms import TextForm
from .models import FeedbackForm


def feedback_form(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_feedback')
    else:
        form = TextForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})


def all_feedback(request):
    feedbacks = FeedbackForm.objects.all()
    return render(request, 'feedback/all_feedback.html', {'feedbacks': feedbacks})


def home(request):
    return render(request, 'feedback/home.html')
