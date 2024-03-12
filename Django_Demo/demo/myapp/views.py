from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TodoItem
import json

# Create your views here.


def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def info(request):
    return render(request, "info.html")

def rsvp(request):
    return render(request, "rsvp.html")

@csrf_exempt
def submit_rsvp(request):
    if request.method == 'POST':

        request_body_json = json.loads(request.body)
        print(request_body_json)
        print(request_body_json.get('full-name'))


        # Process the data received from the front end
        name = request_body_json.get('full-name')

        # TODO: process and save data to the database

        return JsonResponse({'message': f'RSVP submitted successfully for {name}'})
    
    # Handle other HTTP methods or invalid requests
    return JsonResponse({'error': 'Invalid request method'})