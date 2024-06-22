from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import PostImage, Posts, FriendRequests, Friends

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields=["content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs.update(
            {
            "class":"form-control pe-4 border-0",
            "rows":"2",
            "data-autoresize":"",
            "placeholder":"Share your thoughts..."
            }
        )




from .models import Comment

class FriendsForm(forms.ModelForm):
    class Meta:
        model = Friends
        fields = '__all__'

class FriendRequestsForm(forms.ModelForm):
    class Meta:
        model = FriendRequests
        fields = '__all__'

