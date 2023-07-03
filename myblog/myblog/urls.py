from django.contrib import admin
from django.urls import path
from myblog.views import register, change_password, home, create_note_view, note_list_view, logout_view,login_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('change_password/', change_password, name='change_password'),
    path('', home, name='home'),
    path('create_note/', create_note_view, name='create_note'),
    path('login/', login_request, name='login'),
    path('note_list/', note_list_view, name='note_list'),
    path('logout/', logout_view, name='logout'),
]
