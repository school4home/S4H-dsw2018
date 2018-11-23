from django.conf.urls import url
from . import views


urlpatterns = [

    # url(r'^formevent/$', views.formevent, name='formevent'),
    url(r'^create_question_text', views.create_question_text, name='create_question_text'),
    url(r'^list_question_text/', views.list_question_text, name='list_question_text'),
    url(r'^edit_question_text/(?P<id>\d+)/$', views.edit_question_text, name='edit_question_text'),
    url(r'^delete_question_text/(?P<id>\d+)/$', views.delete_question_text, name='delete_question_text'),

]
