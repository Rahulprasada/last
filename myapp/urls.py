from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.first, name = 'one'),
    path('login/', views.login, name="login"),
    path('signup/', views.signup,name="signup"),
    path('success', views.success,name="success"),
    path('dashboard/', views.dash, name='dashboard'),
    path('signalview/', views.sigview, name='signalview'),
    path('stockview/', views.stockview, name="stockview"),
    path('fetch_filtered_data/', views.fetch_filtered_data, name='fetch_filtered_data'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
