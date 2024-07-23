from django.urls import path
from . import views
urlpatterns = [
    path('settings/',views.settings, name="settings"),
    path('<str:cx_user>/friend-list/', views.friends, name='friends'),
    path('<str:cx_user>/photos/', views.photos, name='cxuphotos'),
    
    # ------ PARTIALS CODE ----------
    path('setting_tabs/<str:option>/',views.setting_tabs, name="setting_tabs"),
    
]