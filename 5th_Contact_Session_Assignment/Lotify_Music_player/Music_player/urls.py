
from django.urls import path


from . import views
app_name = 'Music_player'

urlpatterns = [

    path('', views.index, name='index'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('dashboard/<slug:slug>/', views.play_music, name='play_music'),

]

