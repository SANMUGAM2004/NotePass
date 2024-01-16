# manager/urls.py
from django.urls import path
from .views import home, notes_list, passwords_list, add_note, add_password,delete_note,delete_password,signup, userlogin, user_home, profile_not_found
from . import views

urlpatterns = [
    path('', home, name='home'),   
    path('notes/', notes_list, name='notes_list'),
    path('passwords/', passwords_list, name='passwords_list'),
    path('add_note/', add_note, name='add_note'),
    path('add_password/', add_password, name='add_password'),
    path('delete_note/<int:note_id>/', delete_note, name='delete_note'),
    path('delete_password/<str:password_id>/', delete_password, name='delete_password'),
    # path('login',views.login_view,name="login"),
    # path('profile',views.profile,name="profile"),
    path('signup/', signup, name='signup'),
    path('userlogin/', userlogin, name='user_login'),
    path('user_home/', user_home, name='user_home'),
    path('profile_not_found/', profile_not_found, name='profile_not_found'),
]
