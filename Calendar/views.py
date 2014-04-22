from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
#import calendarAPI as api

# Create your views here.

@require_http_methods(["GET"])
def home(request):
    if request.session.has_key("username"):
        context = {
            "username" : request.session["username"],
            "calendars" : ["Leisure", "Work", "School", "General", "Vanderbilt"],
            "events" : ["My Event #1", "My Event #2", "My Event #3", "My Event #4", "My Event #1", "My Event #2", "My Event #3", "My Event #4", "My Event #1", "My Event #2", "My Event #3", "My Event #4", "My Event #1", "My Event #2", "My Event #3", "My Event #4", "My Event #1", "My Event #2", "My Event #3", "My Event #4", "My Event #1", "My Event #2", "My Event #3", "My Event #4", "My Event #1", "My Event #2", "My Event #3", "My Event #4", "My Event #1", "My Event #2", "My Event #3", "My Event #4"]
        }
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
        res = True

        if res is not False:
            request.session["username"] = username
            return redirect('Calendar:home')
        else:
            return HttpResponse("Bad username/password combo")

    else:
        return HttpResponse("Bad request")

                    
@require_http_methods(["POST"])
def signup(request):
    if request.POST.has_key("username") and request.POST.has_key("password") and request.POST.has_key("password2"):
        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        
        if password == password2:
#            res = api.registerUser(username, password)

            request.session["username"] = username
        else:
            return HttpResponse("passwords must match")
        
        return redirect('Calendar:home')
    
    else:
        return HttpResponse("Bad request")

@require_http_methods(["GET"])
def signout(request):
    if request.session.has_key("username"):
        del request.session["username"]
    return redirect('Calendar:home')

def edit_event(request):
    return redirect('Calendar:home')
