from django.conf.urls import url

from . import views

app_name = 'matching'
urlpatterns = [
    url(r'^matches$', views.HelpRequestMatchView.as_view(), name='list-matches'),
]
