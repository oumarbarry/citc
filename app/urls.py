from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('formations', views.formations, name='formations'),
    path('formations/<str:titre>', views.detail_formation, name='detail_formation'),
    path('events', views.events, name='events'),
    path('events/<str:titre>', views.single_events, name='single_events'),
    path('news', views.news, name='news'),
    path('news/<str:titre>', views.single_news, name='single_news'),
    path('<str:titre>', views.citc, name='citc'),      
]