# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from blog.models import *
from django.template import RequestContext

cases = Cases.objects.all()

def index(request):

    return render_to_response('timeline.html', {
        'cases' : cases,
    },
    context_instance = RequestContext(request),
    )

#def justice_list(request):
#
#    return render_to_response('justice_list.html', {
#    },
#    )

def justice(request, slug):

    return render_to_response('justice.html', {
    },
    )

#def category_list(request):
#
#    return render_to_response('category_list.html', {
#    },
#    )

def category(request, slug):

    return render_to_response('category.html', {
    },
    )

def case(request, slug):

    return render_to_response('case.html', {
    },
    )

#def case_list(request):
#
#    return render_to_response('case_list.html', {
#    },
#    )
