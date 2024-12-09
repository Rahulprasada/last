from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name = 'one'),
    path('login/', views.login, name="login"),
    path('signup/', views.signup,name="signup"),
    path('success', views.success,name="success"),
    path('dashboard/', views.dash, name='dashboard'),
    path('signalview/', views.sigview, name='signalview'),
    path('stockview/', views.stockview, name="stockview"),
    path('fetch_filtered_data/', views.fetch_filtered_data, name='fetch_filtered_data'),
]
