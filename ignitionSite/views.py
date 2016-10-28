from django.http import HttpResponse
from django.template.loader import get_template
from django import template

def test(request, queryString) :
    myView = get_template('testShow.html')
    myContext = template.Context({'mystring' : queryString})
    return HttpResponse(myView.render(myContext))
