from django.conf.urls import  handler404, handler500
from quiz.views import *
from quiz import views as quiz_views
from django.urls import path

from django.conf.urls import url
from . import views

app_name = 'quiz'

urlpatterns = [
    path('home', home, name='home'),
    #url(r'^home$', views.home, name='home'),
    url(r'^user-home$', views.user_home, name='user_home'),
    url(r'^play/$', views.play, name='play'),
    url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
    url(r'^submission-result/(?P<attempted_question_pk>\d+)/', views.submission_result, name='submission_result'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^register/', views.register, name='register'),

]


handler404 = quiz_views.error_404
handler500 = quiz_views.error_500