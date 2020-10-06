from django.urls import path
from sim_rating import views

urlpatterns = [
    path('', views.main, name='main'),
    path('sim_rates/a', views.SimRateView1, name='similarity-rates'),
    path('sim_rates/b', views.SimRateView1, name='similarity-rates2'),
    path('sim_rates/c', views.SimRateView1, name='similarity-rates3'),
    path('sim_rates/d', views.SimRateView1, name='similarity-rates4'),
    path('sim_rates/e', views.SimRateView1, name='similarity-rates5'),
    path('sim_rates/f', views.SimRateView1, name='similarity-rates6'),
    path('sim_rates/end', views.end, name='end'),
    
    ]
