from django.conf.urls import url
from .views import LoginView
from .views import NewUserView

urlpatterns = [
    url(r'newuser/', NewUserView.as_view(), name='newuser'),
    url(r'login/', LoginView.as_view(), name='login'),
]
