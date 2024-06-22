from .utilities import login_required, login_requirements
from .forms import CreatePostForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse

from app_users.models import Profile
from .models import Posts, Like, Comment, FriendRequests, Friends
from .forms import FriendRequestsForm,FriendsForm
from django.http import JsonResponse

@login_requirements()
def like_post(request, post_id):
    post = get_object_or_404(Posts, uid=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user.profile)
    if not created:
        like.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_requirements()
def homepage(request):
    profile = request.user.profile
    all_post = Posts.objects.all()
    people = Profile.objects.all()
    request_lists = [ x.author for x in FriendRequests.objects.filter(sender = profile) ]
    existing_friend_object = Friends.objects.filter(author=profile).first()
    friends = existing_friend_object.friend.all() if existing_friend_object else None
    
    got_requests = FriendRequests.objects.filter(author=profile)

    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            the_form = form.save(commit=False)
            the_form.author=profile
            the_form.save()
            return redirect(request.path)
    else:
        form = CreatePostForm()


    context = {
        "posts":all_post,
        "people":people,
        "request_list":request_lists,
        "got_requests":got_requests,
        "friends":friends,
        "form":form,
    }
    return render(request, "home/main/index.html", context)

@login_requirements()
def accept_request(request, usr):
    profile = request.user.profile
    try:
        person = get_object_or_404(Profile, user__username=usr.strip())

        # ---- LOGGED IN USER'S FRIEND ADDING ----->>
        existing_object = Friends.objects.filter(author=profile).first()
        if not existing_object:
            friend_list = Friends.objects.create(author=profile)
            friend_list.friend.add(person)
            friend_list.save()
            FriendRequests.objects.filter(sender=person, author=profile).delete()
            


            
            print("------------ CREATED AND ACCEPTED ----------")

        else:
            existing_object.friend.add(person)
            print("===== EXISTS SO ADDED FRIEND =====")
            FriendRequests.objects.filter(sender=person, author=profile).delete()

        # ---- ALSO ADDING FRIEND FOR THAT PERSON WHO REQUESTED ---->>>
        persons_existing_object = Friends.objects.filter(author=person).first()
        if not persons_existing_object:
            his_friend_list = Friends.objects.create(author=person)
            his_friend_list.friend.add(profile)
            his_friend_list.save()

            FriendRequests.objects.filter(author=person, person=profile).delete()
            print("------------ HIS CREATED AND ACCEPTED ----------")

        else:
            persons_existing_object.friend.add(profile)
            FriendRequests.objects.filter(author=person, person=profile).delete()
            print("===== HIS ALREADY EXISTS SO ADDED FRIEND =====")

    except Exception as e:
        print("ERROR ---->>>>>> ", e)

    return redirect("homepage")


@login_requirements()
def send_friend_request(request):
    if request.method == "POST":
        try:
            person = request.POST.get("the_person")
            author_whom_sending_request = get_object_or_404(Profile, user__username=person.strip())
            
            # Check if the friend request already exists
            existing_request = FriendRequests.objects.filter(
                author=author_whom_sending_request,
                sender=request.user.profile
            ).exists()
            
            if not existing_request:
                FriendRequests.objects.create(
                    author=author_whom_sending_request,
                    sender=request.user.profile,
                    requested=True
                )
                print("SUCCESS SEND REQUEST")
            else:
                print("FRIEND REQUEST ALREADY EXISTS")
            
            # Redirect back to the referring page
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        except Exception as e:
            print(e)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_requirements()
def create_post(request):

    if request.method == "POST":
        form = CreatePostForm(request.POST)
    else:
        form = CreatePostForm()
    context = {
        "form":form,
    }
    # if request.htmx:
    #     return render(request, "home/partials/create_post.html", context)
    # return render(request, "home/create_post.html", context)
    return render(request, "home/partials/create_post.html", context)


@login_requirements()
def view_one_post(request, p_id):
    context={}
    try:
        data = get_object_or_404(Posts, uid=p_id.strip())
        context["data"]=data

    except Exception as e:
        print("PROBLEM====>>> ",e)
    
    return render(request, "home/main/view_single_post.html", context)


@login_requirements()
def view_replies(request, cmnt_uid):
    if request.htmx:
        comment = get_object_or_404(Comment,uid=cmnt_uid.strip())
        
        context={
            "comment":comment
        }
        return render(request, "home/partials/reply.html", context)
    
    return HttpResponse("Noting to show with this url",status=400)


@login_requirements()
def view_comments(request, post_uid):
    if request.htmx:
        post = get_object_or_404(Posts,uid=post_uid.strip())
        if request.method=="POST":
            try:
                # PROBLEM-- object comment not creating
                profile= request.user.profile
                comment=request.POST.get['content']
                Comment.objects.create(
                    user=profile,
                    post=post,
                    content=comment
                )
            except Exception as e:
                print("ERROR ===>> ",e)
        
        context={
            "data":post
        }

        return render(request, "home/partials/comments.html", context)
    
    return HttpResponse("Noting to show with this url",status=400)



# =============== TEMPRORARY TESTING ROUTE ====================

def temp(request):
    post = get_object_or_404(Posts, uid="e66631fe-150d-4db0-8b87-8303be5ba922")
    context = {
        "data": post
    }
    return render(request, "temp.html", context)

def temp_partial(request):
    if request.htmx:
        return render(request, "temp_p.html")
    return redirect("homepage")