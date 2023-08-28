"""users urls."""
#django
from re import template
from django.urls import path


#views
from users import views

urlpatterns = [
    #Posts
    path(
    route= 'profile/<str:username>/',
    view=views.UserDetailView.as_view(),
    name='detail'
    ),
    # Management
    path(
        route= 'login/',
        view= views.login_view, 
        name='login'
    ),

    path(
        route= 'logout/',
        view= views.logout_view ,
        name='logout'
    ),

    path(
        route='signup/',
        view= views.signup,
        name='signup'
    ),

    path(
        route= 'me/profile',
        view= views.update_profile, 
        name='update'
    )
]


