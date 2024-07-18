from .utilities import login_requirements
from .forms import CreatePostForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages

from app_users.models import Profile
from .models import Posts, Like, Comment, FriendRequests, Friends
from .forms import FriendRequestsForm,FriendsForm


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
            messages.success(request, "Post uploaded!")
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
            
            messages.success(request, f" {person} friend request accepted!")

        else:
            existing_object.friend.add(person)
            messages.success(request, f" {person} friend added!")
            FriendRequests.objects.filter(sender=person, author=profile).delete()

        # ---- ALSO ADDING FRIEND FOR THAT PERSON WHO REQUESTED ---->>>
        persons_existing_object = Friends.objects.filter(author=person).first()
        if not persons_existing_object:
            his_friend_list = Friends.objects.create(author=person)
            his_friend_list.friend.add(profile)
            his_friend_list.save()

            FriendRequests.objects.filter(author=person, person=profile).delete()
            # print("------------ HIS CREATED AND ACCEPTED ----------")

        else:
            persons_existing_object.friend.add(profile)
            FriendRequests.objects.filter(author=person, person=profile).delete()
            # print("===== HIS ALREADY EXISTS SO ADDED FRIEND =====")

    except Exception as e:
        messages.error(request, f" {e} !")

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
                messages.success(request, "SUCCESS SEND REQUEST!")
                
            else:
                messages.error(request, "FRIEND REQUEST ALREADY EXISTS!")
                
            
            # Redirect back to the referring page
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        except Exception as e:
            messages.warning(request, f"{e}")
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# @login_requirements()
# def create_post(request):

#     if request.method == "POST":
#         form = CreatePostForm(request.POST)
#     else:
#         form = CreatePostForm()
#     context = {
#         "form":form,
#     }
#     # if request.htmx:
#     #     return render(request, "home/partials/create_post.html", context)
#     # return render(request, "home/create_post.html", context)
#     return render(request, "home/partials/create_post.html", context)


@login_requirements()
def view_one_post(request, p_id):
    context={}
    try:
        data = get_object_or_404(Posts, uid=p_id.strip())
        context["data"]=data

    except Exception as e:
        messages.error(request, f" {e}!")
    
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
def create_comments(request, post_uid):
    if request.htmx:
        if request.method == "POST":
            post = get_object_or_404(Posts, uid=post_uid.strip())
            
            try:
                comment_content = request.POST.get('content')                
                
                if comment_content:
                    profile = request.user.profile
                    Comment.objects.create(
                        user=profile,
                        post=post,
                        content=comment_content
                    )
            except Exception as e:
                messages.success(request, f" {e}!")
        
        context = {
            "data": post
        }
        return render(request, "home/partials/comments.html", context)
    
    return HttpResponse("Nothing to show with this url", status=400)


@login_requirements()
def create_reply(request, cmnt_uid):
    parent_comment = Comment.objects.get(uid=cmnt_uid.strip())
    if request.htmx:
        context = {
            "parent":parent_comment
        }
        return render(request, "home/partials/reply_form.html", context)
    
    return HttpResponse("Nothing to show with this url", status=400)

@login_requirements()
def add_reply(request):
    if request.htmx:
        if request.method=="POST":
            try:
                the_reply=request.POST.get('the_reply')
                main_post_uid=request.POST.get('main_post')            
                parent_comment_uid=request.POST.get('parent_comment')            
                parent_comment = get_object_or_404(Comment, uid=parent_comment_uid.strip())
                the_post=get_object_or_404(Posts, uid=main_post_uid.strip())
                Comment.objects.create(
                    post=the_post,
                    user=request.user.profile,
                    content=the_reply,
                    parent=parent_comment,
                )
            except Exception as e:
                messages.error(request, f" {e}!")

        context={
            "data":the_post
        }
        return render(request, "home/partials/comments.html", context)
    
    return HttpResponse("Nothing to show with this url", status=400)


@login_requirements()
def make_a_post(request):

    if request.htmx:
        if request.method=="POST":
            form=CreatePostForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    the_form = form.save(commit=False)
                    the_form.author = request.user.profile
                    the_form.save()
                    return redirect("homepage")
                except Exception as e:
                    messages.error(request, f" {e} !")
        else:
            form=CreatePostForm()
        context={"form":form}
        
        return render(request, "home/partials/post_form.html", context)
    else:
        return HttpResponse("Nothing to show with this url", status=400)

# -----------------------------------
@login_requirements()
def like_post(request, post_id):
    post = get_object_or_404(Posts, uid=post_id)
    like, created = Like.objects.get_or_create(post=post, user=request.user.profile)
    if not created:
        like.delete()
    if request.htmx:
        context={
            "data": post,

        }
        return render(request, "home/partials/liked.html", context)
    else:
        return HttpResponse("Go Back some server misleading!")


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