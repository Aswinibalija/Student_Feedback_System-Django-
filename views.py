

# Create your views here.
from django.shortcuts import render, redirect
from .models import Feedback
from django.utils import timezone

def submit_feedback(request):
    if request.method == "POST":
        std_name = request.POST['std_name']
        email = request.POST['email']
        course = request.POST['course']
        rating = request.POST['rating']
        message = request.POST['message']

        Feedback.objects.create(
            std_name=std_name,
            email=email,
            course=course,
            rating=rating,
            message=message,
            timestamp=timezone.now()
        )
        return render(request, 'thank_you.html')

    return render(request, 'feedback_form.html')
