from django.urls import path
from . import views
urlpatterns = [
    path('settings/',views.settings, name="settings"),

    # ------ PARTIALS CODE ----------
    path('setting_tabs/<str:option>/',views.setting_tabs, name="setting_tabs"),
    
    path('testing/',views.tempp, name="tempp"),
]