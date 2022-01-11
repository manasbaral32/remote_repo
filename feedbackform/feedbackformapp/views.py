from django.shortcuts import render
from .models import FeedbackData

# Create your views here.
def feedback_view(request):
    if request.method == "GET":
        feedbacks = FeedbackData.objects.all()
        return render(request, 'feedbackform.html',{'feedbacks':feedbacks})
    else:
       name1 = request.POST.get('name1')
       
       feedback1 = request.POST.get('feedback1')

       FeedbackData(
           name=name1,
           feedback=feedback1
       ).save()
       return render(request, 'feedbackform.html')