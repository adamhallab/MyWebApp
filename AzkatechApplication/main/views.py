from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import NewUserForm, VacationForm
from django.contrib.auth import login
from django.contrib import messages #import messages
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Vacation
# Create your views here.

def home(response):
    vacation = Vacation.objects.filter(user=response.user) #displaying vacations of specific user
    return render(response, "main/home.html", locals())

def add(request):
    if not request.user:
        return redirect('/login')
    form = VacationForm()
    if request.method=="POST":
        form = VacationForm(data=request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user #I did this to save the data under the user that is logged in.
            submission.save()
            return redirect('/home')
    return render(request, 'main/add.html', locals())

def register_request(request): #This displays a form to create a new user
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Registration successful.')
			return redirect("/home")
		messages.error(request, 'Unsuccessful registration. Invalid information.')
	form = NewUserForm
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request): #This is the login form
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, 'You are now logged in as {username}.')
                return redirect("/home")
            else:
                messages.error(request,'Invalid username or password.')
        else:
            messages.error(request,'Invalid username or password.')
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request): #Logging out
    logout(request)
    messages.info(request, 'You have successfully logged out.') 
    return redirect("/login")

def VacationUpdate(request, pk): #This is for editing an existing vacation, by filling in the form already with info using the appropriate ID, then altering it when a user makes a change.
    if not request.user:
        return redirect('/login')
    obj = Vacation.objects.get(id=pk)
    form = VacationForm(instance=obj)
    if request.method == 'POST':
        form = VacationForm(data=request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('/home')
    return render(request, 'main/add.html', locals())

def VacationDelete(request, pk): #This simply deletes the row of the appropriate ID.
    if not request.user:
        return redirect('/login')
    obj = get_object_or_404(Vacation, id=pk)
    obj.delete()
    return redirect('/home')