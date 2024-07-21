from .utilities import login_requirements
from .forms import CreatePostForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages

from app_users.models import Profile
from .models import Posts, Like, Comment, FriendRequests, Friends
from .forms import FriendRequestsForm,FriendsForm


@login_requirements()
def homepage(request):
    # current loged in user profile
    profile = request.user.profile

    all_post = Posts.objects.all()
    # we can add logic here to recomend the friend suggestion
    people = Profile.objects.all()

    # Filtering the friend request sended list to show in template
    my_requests = FriendRequests.objects.filter(sender = profile)
    request_lists = [ x.author for x in my_requests ]
    
    
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
        # "my_requests":my_requests.filter(accepted=False),
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
            
            messages.success(request, f" {person}'s friend request accepted!")

        else:
            existing_object.friend.add(person)
            messages.success(request, f"{person} added as friend!")
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
                messages.error(request, "Already in friend request list!")
                
            
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
                    messages.success(request,"You added a comment")
            except Exception as e:
                messages.warning(request, f" {e}!")
        
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


# ---- WORKING - FROM - 18/07/2024 ----- (DONE)
# NOTE: The search functionality can be improved after develop Pages and Groups feature.
# CAN IMPROVE: 2
# ERROR/Bug: 0
@login_requirements()
def search(request):
    '''
    SEARCH FUNCTION - No parameter needed.
    This funtion takes the search argument via GET method from the webpage
    and match the charecter with username contains in the matched query or not.
    '''
    profile = request.user.profile
    q = request.GET.get('q')
    results = []
    frnd_reqs = FriendRequests.objects.filter(sender=profile, accepted=False)
    got_reqs = FriendRequests.objects.filter(author=profile, accepted=False)
    
    if q:
        # HERE HAVE TO IMPROVE TO FIND THE USER WITH MULTIPLE - username, f_name, L-name >>
        # results = Profile.objects.filter(profile__user__username__icontains=q)
        results = Profile.objects.filter(user__username__icontains=q)
        try:
            print(results)
            print(frnd_reqs)

        except Exception as e:
            print(dir(results))
            print(e)

    context={
        "search_results":results,
        "s_query":q,
        "frnd_reqs":[ x.author for x in frnd_reqs],
        "got_reqs": [ x.sender for x in got_reqs],
    }

    return render(request, "home/main/search.html", context)


# ---- WORKING - FROM - 19/07/2024 ----- (DONE)
# NOTE: Nothing
# CAN IMPROVE: 2  | i) like to the comment ii) load more comment
# ERROR/Bug: 1    | i) reply need to show 

@login_requirements()
def feed_comment(request, post_uid):
    if request.htmx:
        post = get_object_or_404(Posts, uid=post_uid.strip())
        if request.method == "POST":
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
                print(f"ERROR - FEED COMMENT: {e}")
                messages.warning(request, f" {e}!")
        try:
            my_comment = Comment.objects.filter(
                user=profile,
                post=post,
                ).order_by("-created_at").first()
            
        except:
            my_comment=None
        context = {
            "data": post,
            "my_comment":my_comment,
        }
        # return redirect("homepage")
        return render(request, "home/partials/feed_comment.html", context)
    return HttpResponse("Don't lost in the --- MORICHIKA ---", status=400)


# ---- WORKING - FROM - 19/07/2024 -----(DONE)
# NOTE: Nothing
# CAN IMPROVE: 2
# ERROR/Bug: 0
from .models import PostImage

@login_requirements()
def view_profile(request, name):
    '''
    The function for view user profile and detail.
    '''
    username = name.strip()
    its_user_himself = False
    profile = get_object_or_404(Profile, user__username = username)
    all_post = Posts.objects.filter(author=profile)
    all_photo = PostImage.objects.filter(post__author = profile)
    if username == request.user.username:
        its_user_himself = True

    context={
        "profile":profile,
        "its_user_himself":its_user_himself,
        "posts":all_post,
        "all_photo":all_photo,
    }
    
    return render(request, "home/main/view_profile.html", context)




# ---- WORKING - FROM - 21/07/2024 -----(RUNNING)
# NOTE: Nothing
# CAN IMPROVE: 3 [i) after delete redirect where it was 
#                ii) Only the post owner will see the delete option in HTML
#               iii) 
# ]
# ERROR/Bug: 0

@login_requirements()
def delete_post(r, p_id):
    '''
    This function taked post uid and check if the user is actually the
    Post's owner or not, then it delete the post.
    '''
    post = get_object_or_404(Posts, uid=p_id.strip())
    if post.author == r.user.profile:
        try:
            post.delete()
            messages.warning(r, "Your post has been deleted permanently!")
        except:
            messages.error(r, "Something fishy happened! Post could not be deleted!")
    else:
        messages.warning(r, "Whatever you do! You can't delete someone's post!")
    return redirect("homepage")

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