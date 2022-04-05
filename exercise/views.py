from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.
def exercise(request):
    context = {}
    if request.method=='POST':
        data = request.POST['data']
        
    return render(request, 'exercise/exercise.html',context)

class ExerciseView(TemplateView):
    template_name = "exercise/exercise.html"