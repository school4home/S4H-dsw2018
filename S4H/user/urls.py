from django.conf.urls import url
from .views import LoginView, logout_user, delete_user
from .views import NewUserView

urlpatterns = [
    url(r'newuser/', NewUserView.as_view(), name='newuser'),
    url(r'login/', LoginView.as_view(), name='login'),
    url(r'logout/', logout_user, name='logout'),
    url(r'delete/$', delete_user, name='deleteuser'),
]
