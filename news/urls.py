from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_news'),
    path('<slug:news_slug>', views.article, name='article'),
    path('<str:club>', views.get_club_news_list, name="club_news_list"),
]