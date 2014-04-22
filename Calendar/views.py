from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
#import calendarAPI as api

# Create your views here.

def home(request):
    if request.session.has_key("username"):
        context = {}
        return render(request, 'Calendar/calendar.html', context)
    else:
        context = {}
        return render(request, 'Calendar/signin.html', context)


@require_http_methods(["POST"])
def signin(request):
    if request.POST.has_key("username") and request.POST.has_key("password"):
        username = request.POST["username"]
        password = request.POST["password"]
    
#        res = api.login(username, password)

    
    else:
        return HttpResponse("Bad request")

                    
@require_http_methods(["POST"])
def signup(request):
    pass
