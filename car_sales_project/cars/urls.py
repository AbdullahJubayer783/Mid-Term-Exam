from django.urls import path
from . import views
urlpatterns = [
    path('deatils/<int:id>/',views.DetailsCarView.as_view(),name='deatils'),
    path('buy_now/<int:id>/', views.buy_now,name='buy_now'),
]