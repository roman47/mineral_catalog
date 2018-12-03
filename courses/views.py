from django.shortcuts import get_object_or_404, render

from .models import Course, Step, Mineral
import random
from django.db.models import Max


def course_list(request):
    courses = Course.objects.all()
    email = 'question@learning_site.com'
    return render(request, 'courses/course_list.html', {'courses': courses,
                                                       'email':email})
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})

def index(request):
    minerals = Mineral.objects.all()
    rand = random_mineral_pk
    return render(request, 'courses/index.html', {'minerals': minerals, 'rand': rand})
  
def detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'courses/detail.html', {'mineral': mineral})
  
def random_mineral_pk():
      '''Gets a random primary key from the mineral table'''
      count = Mineral.objects.latest('pk').pk
      random_index = random.randint(0, count - 1)
      return random_index