from django import template
from django.utils.safestring import mark_safe

import markdown2

import random
from django.db.models import Max

from courses.models import Course,Mineral

register = template.Library() 

@register.simple_tag
def newest_course():
    '''Gets the most recent course that was added to the library'''
    return Course.objects.latest('created_at')

@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list(): 
    '''Returns dictionary of courses to display as navigation pane'''
    courses = Course.objects.all()
    return {'courses': courses}

@register.filter('time_estimate')
def time_estimate(word_count):
    '''Estimates the number of minutes to complete a step based on word count'''
    minutes = round(word_count/20)
    return minutes

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''Converts markdown text to html'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
  
@register.simple_tag
def random_mineral_pk():
      '''Gets a random primary key from the mineral table'''
      count = Mineral.objects.latest('pk').pk
      random_index = random.randint(0, count - 1)
      return random_index
    