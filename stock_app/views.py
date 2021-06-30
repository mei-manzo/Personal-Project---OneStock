from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.db.models import Count
import requests
from bs4 import BeautifulSoup

def index(request):
    return render(request, "index.html")

def check_registration(request):
    errors = User.objects.basic_validator(request.POST)
    email = request.POST['email']
    if request.method == "GET":
        return redirect('/')
    elif len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    #changed to check len of dictionary
    elif len(User.objects.filter(email=email)) >= 1:
        messages.error(request, "Email is already in use")
        return redirect('/')
    else:
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name = request.POST['first-name'], last_name = request.POST['last-name'], username = request.POST['username'], email = request.POST['email'], password = hashed_pw)
        request.session['user_id'] = new_user.id
        return redirect('/success')

def check_login(request):
    if request.method == "GET":
        return redirect ("/")
    else:
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/success')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id = request.session['user_id'])
    context = {
        "current_user" : this_user[0].first_name,
        }
    return render(request, "dashboard.html", context)

def feed_parser(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id = request.session['user_id'])
    URL = 'https://www.google.com/search?q=beyond+meat&rlz=1C1CHBF_enUS898US898&sxsrf=ALeKk00IH9jp1Kz5-LSyi7FUB4rd6--_hw:1624935518812&source=lnms&tbm=nws&sa=X&ved=2ahUKEwicqIbD7LvxAhVWo54KHXgRA9oQ_AUoAXoECAEQAw&biw=1536&bih=754'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    headers = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')
    header_dict = []
    for h in headers:
        # header_dict = []
        header_dict.append(h.text)
        context = {
            "current_user" : this_user[0].first_name,
            "header_dict": header_dict,
        }
    return render(request, "feed.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')