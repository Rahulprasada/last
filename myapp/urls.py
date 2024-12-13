from django.urls import path # type: ignore
from . import views
from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore

urlpatterns = [
    path('', views.first, name = 'one'),
    path('login/', views.login, name="login"),
    path('signup/', views.signup,name="signup"),
    path('success', views.success,name="success"),
    path('dashboard/', views.dash, name='dashboard'),
    path('signalview/', views.sigview, name='signalview'),
    path('stockview/', views.stockview, name="stockview"),
    path('fetch_filtered_data/', views.fetch_filtered_data, name='fetch_filtered_data'),
    path('excelfile/',views.stock_view,name='excelfile'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
