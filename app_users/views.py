from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import CommonRegistrationForm, ProfileForm
from .models import Profile


# Create your views here.
def registration(request):
    if request.method == "POST":
        form = CommonRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Register done!")
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
            messages.success(request,"Congrats! Your account is complete.")
            return redirect("homepage")
        else:
            messages.error(request, form.errors)
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
    if request.user.is_authenticated:
        messages.warning(request,"You are already loggedIn !")
        return redirect("homepage")
    if request.POST:
        username_or_email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = authenticate(email=username_or_email, password=password)
            login(request, user)
            messages.success(request, "Log in success! Welcome.")
            # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            # NOTE: Here we can update as - if some user was in another page but loggedout and 
            #       Want to login and see that page where he was needed to be logged in, 
            #       not redirect to homepage
            return redirect("homepage")
        
        except Exception as e:
            messages.error(request,f"ERROR: {e}")
            messages.error(request,"May be credentials not valid!")

    return render(request, "auth/login.html")