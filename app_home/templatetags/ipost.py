from django import template
from app_home.models import Posts, Friends

register = template.Library()

@register.filter
def mypost(inputs):
    try:
        no_of_post = Posts.objects.filter(author=inputs)
    except:
        pass
    if no_of_post:
        return no_of_post.count()
    else:
        return 0

@register.filter
def myfiends(user):
    try:
        no_of_frnd = Friends.objects.get(author=user)
        return no_of_frnd.friend.count()

    except Exception as e:
        print(e)
        return 0

