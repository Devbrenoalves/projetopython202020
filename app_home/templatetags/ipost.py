from django import template
from app_home.models import Posts, Friends, FriendRequests

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

@register.filter
def mefollow(user):
    try:
        no_of_frnd = FriendRequests.objects.filter(sender=user, accepted=False)
        return no_of_frnd.count()

    except Exception as e:
        print(e)
        return 0

    

@register.filter(name='add_class')
def add_class(value, arg):
    css_classes = value.field.widget.attrs.get('class', '')    
    if css_classes:
        css_classes += ' ' + arg
    else:
        css_classes = arg

    css_name = value.field.widget.attrs.get('name', '')    
    if css_name:
        css_name += ' ' + "image---11"
    else:
        css_name = "image---11"
        
    value.field.widget.attrs['class'] = css_classes
    value.field.widget.attrs['name'] = css_name
    return value