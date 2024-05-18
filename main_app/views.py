from django.conf import settings
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RsvpEntry
import json
import os

# Create your views here.


def home(request):
    return render(request, "home.html")

def directions(request):
    return render(request, "directions.html")

def itinerary(request):
    return render(request, "itinerary.html")

def photos(request):
    return render(request, "photos.html")

def info(request):
    return render(request, "info.html")

def people(request):
    return render(request, "people.html")

def rsvp(request):
    return render(request, "rsvp.html")

def thanks_accepted(request):
    return render(request, "thanks_accepted.html")

def thanks_declined(request):
    return render(request, "thanks_declined.html")

def password_entry(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        hashed_password = os.environ.get('HASHED_PASSWORD')
        if check_password(password, hashed_password):
            request.session['password_entered'] = True
            request.session.set_expiry(settings.SESSION_COOKIE_AGE)
            return redirect('home')
        else:
            messages.error(request, 'Incorrect password')
    return render(request, 'password_entry.html')

@csrf_exempt
def get_invite(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        print(name)

        try:
            # get the current invite from the database
            current_invite = RsvpEntry.objects.get(name__iexact=name)
            print(current_invite)
            print(current_invite.name)
            print(current_invite.attending)
            print(current_invite.invite)

            if not current_invite:
                return JsonResponse({'error': 'No invite found for given name.'}, status=404)
            
            invite_id = current_invite.invite

            # get all users on the invite
            all_users_on_invite = RsvpEntry.objects.filter(invite=invite_id)
            print("All users on invite: ")
            print(all_users_on_invite)
            print(list(all_users_on_invite.values()))

            return JsonResponse({
                'all_users_on_invite': list(all_users_on_invite.values())
            })

        except RsvpEntry.DoesNotExist:
            return JsonResponse({'error': 'No invite found for given name.'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def submit_rsvp(request):
    print("In submit_rsvp")

    if request.method == 'POST':
        print("In submit_rsvp POST method")

        request_body_json = json.loads(request.body)
        print("On the server side: ")
        print(request_body_json)
        
         # Process the data received from the front end
        for form in request_body_json:
            print(form)
            print(form.get('full-name'))
            print(form.get('attending'))

            current_rsvp = RsvpEntry.objects.get(name=form.get('full-name'))

            if not current_rsvp:
                return JsonResponse({'error': 'No RSVP found for given name.'}, status=404)

            # Data validation
            if not form.get('full-name'):
                return JsonResponse({'error': 'Full name is required'}, status=400)
            
            if form.get('attending') not in ['accepted', 'decline']:
                return JsonResponse({'error': 'Invalid value for attending.'}, status=400)
            
            if current_rsvp.invite is None:
                return JsonResponse({'error': 'No invite found for given name.'}, status=404)

            current_rsvp.attending = form.get('attending')
            current_rsvp.meal = form.get('food-preference')
            current_rsvp.dietary_restrictions = form.get('dietary-restrictions')
            current_rsvp.song_request = form.get('song-request')
            current_rsvp.babysitter = form.get('babysitter')
            current_rsvp.welcome_dinner = form.get('welcome-dinner')
            current_rsvp.welcome_meal = form.get('welcome-meal')
            current_rsvp.pizza = form.get('pizza')
            current_rsvp.pizza_meal = form.get('pizza-meal')
            current_rsvp.stay = form.get('stay')

            try:
                current_rsvp.save()
            except Exception as e:
                return JsonResponse({'error': f'Error saving RSVP: {str(e)}'}, status=500)
        
        return JsonResponse({'message': f'RSVP submitted successfully for  {form.get("full-name")}'})
    
    # Handle other HTTP methods or invalid requests
    return JsonResponse({'error': 'Invalid request method'})