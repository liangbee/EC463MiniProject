from django.shortcuts import render, redirect
from catalog.models import HouseRoom,Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth import login, authenticate
from catalog.forms import SignUpForm



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            print(user)
            number_of_rooms = form.cleaned_data.get('number_of_rooms')
            user.save()
            current_user=User.objects.get(username=user)
            current_user_id=current_user.id
            profile = Profile.objects.create(user_id=current_user_id, number_of_rooms=number_of_rooms)
            profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



@login_required
def index(request):
    temp_dict = {}
    humid_dict = {}
    current_user_id=request.user.id
    current_username=request.user.username
    number_rooms=Profile.objects.filter(user_id=current_user_id).values_list('number_of_rooms')[0][0]
    for x in range (1,number_rooms+1):
        temp_dict[x]=random.uniform(20,25)
        humid_dict[x]=random.uniform(25,60)

    context = {
        'number_rooms': number_rooms,
        'username': current_username,
        'temp_readings': temp_dict,
        'humid_readings': humid_dict,
    }

    return render(request, 'index.html', context=context)
