from django.shortcuts import render, HttpResponse, redirect
from app_users.models import Profile
from app_users.forms import ProfileForm
from django.contrib import messages
from app_home.utilities import login_requirements


@login_requirements()
def settings(request):
    return render(request, "settings/main/settings.html")


# 20-07-2024 ----- (DONE)
# IMPROVE: 3
# ERROR: Here as i used HTMX so form saves good but image don't -- Need Fix
@login_requirements()
def setting_tabs(request, option):
    if request.htmx:
        profile=request.user.profile
        if option=="profile":
            if request.method == "POST":
                form = ProfileForm(request.POST, request.FILES, instance=profile)                
                if form.is_valid():
                    form.save()
                    messages.success(request,"Profile was updated successfully!")
                    return redirect("setting_tabs", option="profile")
                else:
                    print(form.errors)
            else:
                form = ProfileForm(instance=profile)
            context = {"form":form}

            return render(request,"settings/partials/profile.html", context)
        
        elif option=="notify":
            
            return render(request,"settings/partials/notify.html")
        
        elif option=="suspend":
            
            return render(request,"settings/partials/delete.html")
        
        elif option=="privacy":

            return render(request,"settings/partials/privacy.html")
        
    return HttpResponse("Are you losted? Go back where you came from!")




# =============== TEST TEMP ------------

def tempp(req):
    if req.method=="POST":
        form = ProfileForm(req.POST, req.FILES, instance=req.user.profile)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form =ProfileForm(instance=req.user.profile)
    context={
        "form":form,
    }
    return render(req, "settings/partials/profile.html" , context)