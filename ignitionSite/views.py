#from django import forms

#from django.http import HttpResponse
#from django.http import HttpResponseRedirect

from django import template

from django.shortcuts import render_to_response

from django.http import JsonResponse

from django.template import RequestContext
#from django.template.loader import get_template

from django.views.decorators.csrf import csrf_exempt

#sfrom singleSignOn.models import Idlusers
from singleSignOn.apps import SinglesignonConfig

#from urllib.parse import urlencode

import adal
import sys

@csrf_exempt
def handleEntry(request, queryString) :
#    myView = get_template('testShow.html')
#    firstRow = Idlusers.objects.first()
#    queryString = SinglesignonConfig.signInURL + urlencode(SinglesignonConfig.signInParameterDictionary)
#    myContext = template.Context({'mystring' : queryString, 'myEMAIL' : firstRow.ssoaccount, 'myusername' : request.POST['myusername'], 'mypassword' : request.POST['mypassword']})
#    myContext = template.Context({'mystring' : queryString, 'myEMAIL' : firstRow.ssoaccount, 'myusername' : 'testuser', 'mypassword' :  '1234'})
#    return HttpResponse(myView.render(myContext))
#    return render_to_response('testShow.html', myContext, RequestContext(request))
#    return render(request, 'testShow.html', myContext)

    context = adal.AuthenticationContext(SinglesignonConfig.authority_uri)
    myusername = request.POST['myusername']
    mypassword = request.POST['mypassword']
    
    try:
        token = context.acquire_token_with_username_password( SinglesignonConfig.client_id, myusername, mypassword, SinglesignonConfig.client_id, SinglesignonConfig.client_secret )
        
        dic = {'returnCode' : 0, 'returnState' : 'Success', 'userId' : token['userId'], 'givenName' : token['givenName'], 'familyName' : token['familyName']}
        myContext = template.Context(dic)
#        return render_to_response('LoginOK.html', myContext, RequestContext(request))
        return JsonResponse(dic)    
    except:
        (errtype, errvalue, tb) = sys.exc_info()
        if errvalue.error_response != None :
            dic = {'returnCode' : -1, 'returnState' : 'LoginFailed', 'userId' : myusername, 'errLog' : str(errvalue.error_response['error_description']), 'errorType' : str(errtype)}
        else:
            dic = {'returnCode' : -1, 'returnState' : 'LoginFailed', 'userId' : myusername, 'errLog' : str(errvalue), 'errorType' : str(errtype)}
        myContext = template.Context(dic)
#        return render_to_response('LoginFailed.html', myContext, RequestContext(request))
        return JsonResponse(dic)    

def handleWelcome(request) :
    return render_to_response('Welcome.html', {}, RequestContext(request))

#def handleLogin(request):
#    if request.method == 'POST':
#        myView = get_template('testShow.html')
#        form = LoginForm(request.POST)
#        if form.is_valid():
#            userlogin = form.save()
#            return HttpResponseRedirect('/testme/' + str(userlogin.pk))


