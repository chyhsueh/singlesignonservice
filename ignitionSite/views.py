from django import forms

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django import template
from django.template.loader import get_template

from singleSignOn.models import Idlusers

def test(request, queryString) :
    myView = get_template('testShow.html')
    firstRow = Idlusers.objects.first()
    
#    myContext = template.Context({'mystring' : queryString, 'myEMAIL' : firstRow.ssoaccount, 'myusername' : request.POST['myusername'], 'mypassword' :  request.POST['mypassword']})

    myContext = template.Context({'mystring' : queryString, 'myEMAIL' : firstRow.ssoaccount, 'myusername' : 'testuser', 'mypassword' :  '1234'})
    return HttpResponse(myView.render(myContext))

#def handleLogin(request):
#    if request.method == 'POST':
#        myView = get_template('testShow.html')
#        form = LoginForm(request.POST)
#        if form.is_valid():
#            userlogin = form.save()
#            return HttpResponseRedirect('/testme/' + str(userlogin.pk))


