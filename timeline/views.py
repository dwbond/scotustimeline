# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from timeline.models import *
from random import randint
from django.shortcuts import get_object_or_404

# though named for "cases", all of these functions will work just as well with justices
"""
def caseNumber(cases):
    return cases.count()

def caseList(cases, totalCases):
    caseList = []
    if totalCases >= 10:
        for i in range(10):
            # get a random number in the range of the number of cases
            # append that case to caseList
            # return caseList
    else:
        for i in range(totalCases - 1):
            # do the same thing

# for the front page, cases will be Case.objects.all() and caseNumber will be the length of all the cases

def timelineChange(begin, end):
    # the user enters a start date and an end date
    # return a list of all the cases in that time range
    
    # try, catch, if len(list) == 1
    # pop up an error

# that new list will be passed to caseList, and ten random ones in he specified section of time will be returned

# THERE'S PROBABLY GOING TO HAVE TO BE A NEW PAGE RENDERED
# SINCE I AIN'T MESSING WITH NO JAVASCRIPT OR AJAX SHIT
"""
def index(request):

    return render_to_response('timeline.html', {
    },
    )
# # # # # # # # # # #
def justice_list(request):

    justices = Justice.objects.all()

    return render_to_response('justice_list.html', {
    },
    )

def justice(request, slug):

    return render_to_response('justice.html', {
        'justice': get_object_or_404(Justice, slug=slug),
    },
    )
# # # # # # # # # # #
def category_list(request):

    categories = Category.objects.all()

    return render_to_response('category_list.html', {
    },
    )

def category(request, slug):

    return render_to_response('category.html', {
        'category': get_object_or_404(Category, slug=slug),
    },
    )
# # # # # # # # # # #
def case(request, slug):

    return render_to_response('case.html', {
        'case': get_object_or_404(Case, slug=slug),
    },
    )

def case_list(request):

    cases = Case.objects.all()

    return render_to_response('case_list.html', {
    },
    )
