from django.http import HttpResponse

def test(request, queryString) :
    return HttpResponse('<html><head><title>Testing page</title></heed><body bgcolor=\"cyan\">Testing! 中文會不會通呢?' + queryString + '</body></html>')

