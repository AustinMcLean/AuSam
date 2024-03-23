from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TodoItem, RsvpEntry
import json

# Create your views here.


def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def directions(request):
    return render(request, "directions.html")

def info(request):
    return render(request, "info.html")

def rsvp(request):
    return render(request, "rsvp.html")

def password_entry(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        hashed_password = 'pbkdf2_sha256$720000$Yl01oPWsAQ8oSoK2UoEqkR$U79iUPNPYODSSBJpa4mmNj2DTjZu7ZBynOMWwfpGtik='
        if check_password(password, hashed_password):
            request.session['password_entered'] = True
            return redirect('home')
        else:
            messages.error(request, 'Incorrect password')
    return render(request, 'password_entry.html')

@csrf_exempt
def submit_rsvp(request):
    if request.method == 'POST':

        request_body_json = json.loads(request.body)
        print(request_body_json)
        print(request_body_json.get('full-name'))


        # Process the data received from the front end
        name = request_body_json.get('full-name')
        response = request_body_json.get('attending')

        # TODO: process and save data to the database
        rsvp_entries = RsvpEntry.objects.all()
        # rsvp_entries = []
        print(rsvp_entries)

        current_rsvp = None
        for entry in rsvp_entries:
            print(entry)
            print(entry.name)
            if name == entry.name:
                entry.attending = response
                current_rsvp = entry

        if not current_rsvp:
            # raise Exception('No invite found for given name.')
            print('No invite found for given name.')

        # current_rsvp = RsvpEntry()
        # current_rsvp.name = name
        # current_rsvp.attending = response
        print(current_rsvp)
        # rsvp_entries.appends(current_rsvp)
        # print(rsvp_entries.name)

        # Insert or Update DB
        current_rsvp.save()

        return JsonResponse({'message': f'RSVP submitted successfully for {name}'})
    
    # Handle other HTTP methods or invalid requests
    return JsonResponse({'error': 'Invalid request method'})