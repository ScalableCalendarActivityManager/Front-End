from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from datetime import date
#import calendarAPI as api

# Create your views here.

@require_http_methods(["GET"])
def home(request):
    if request.session.has_key("username"):
        events = []
        
        for i in range(1,51):
            n = i % 4 * 15
            if n is 0:
                thestr = "00"
            else:
                thestr = str(n)
            
            n2 = i%37%12
            
            if n2 is 0:
                n2+=12
                    
                    
            n3 = i%12
            
            if n3 is 0:
                n3 += 12
            
            n4 = i%28
            
            if n4 is 0:
                n4 += 28
            
            events.append({
                "name" : "My Event #"+str(i),
                "date" : date(2014, n3, n4),
                "time" : str(n2)+":"+thestr+" pm"
            })

        context = {
            "username" : request.session["username"],
            "calendars" : ["Leisure", "Work", "School", "General", "Vanderbilt"],
            "events" : sorted(events)
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
