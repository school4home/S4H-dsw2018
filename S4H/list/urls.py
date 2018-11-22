from django.conf.urls import url
from . import views


urlpatterns = [

    # url(r'^formevent/$', views.formevent, name='formevent'),
    url(r'^create_question_text', views.create_question_text, name='create_question_text'),

]
