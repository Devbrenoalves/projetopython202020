from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

from .forms import CommonRegistrationForm, ProfileForm
from .models import Profile


# Create your views here.
def registration(request):
    if request.method == "POST":
        form = CommonRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Register done!")
            return redirect("login_page")
    else:
        form = CommonRegistrationForm()
    context = {
        "form":form
    }
    return render(request, "auth/signup.html", context)

@login_required
def registration_step2(request):
    try:
        profile = request.user.profile
    except:
        profile = Profile.objects.create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            the_form = form.save(commit=False)
            the_form.fill_up = True
            the_form.registered = True
            the_form.save()
            return redirect("homepage")
    else:
        form = ProfileForm(instance=profile)
    context = {
        "form":form
    }
    return render(request, "auth/signup.html", context)

def logout_view(request):
    logout(request)
    return redirect("homepage")

def login_page(request):
    if request.POST:
        username_or_email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = authenticate(email=username_or_email, password=password)
            login(request, user)
            return redirect("homepage")
        
        except Exception as e:
            print("ERROR+=> ",e)

    return render(request, "auth/login.html")