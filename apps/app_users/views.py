from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import CommonRegistrationForm, ProfileForm
from .models import Profile

from .utils import send_welcome_email

def registration(request):
    if request.method == "POST":
        form = CommonRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            login(request, user)
            messages.success(request, "Register done!")

            # sending welcome email by celery task
            # ---->> Uncomment [Cz I am using pythonanywhere🤦‍♂️]<<----
            try:
                # from .tasks import async_send_welcome
                # async_send_welcome.delay(user.uid)
                send_welcome_email(user.email, user.username)

            except Exception as exc:
                import logging
                logging.exception("Could not send welcome email", exc_info=exc)
                print(f"Error sending welcome email: {exc}")
                
            messages.success(request, "Welcome to Bloome! Please complete your profile.")

            return redirect("signup_details")
    else:
        form = CommonRegistrationForm()

    return render(request, "auth/signup.html", {"form": form})


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

            #  -- IMPEMENTED Improvement --
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            
            return redirect("homepage")
        
        except Exception as e:
            messages.error(request,f"ERROR: {e}")
            messages.error(request,"May be credentials not valid!")

    return render(request, "auth/login.html")




def demo_login(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already loggedIn !")
        return redirect("homepage")
    
    # demo user credentials
    email = "demo@gmail.com"
    password = "demo1234"

    user = authenticate(email=email, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Demo login success! Welcome.")
        return redirect("homepage")
    else:
        messages.error(request, "Demo login failed. Please try again.")
        return redirect("login_page")