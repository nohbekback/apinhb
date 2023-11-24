from django.urls import path
from . import views



urlpatterns = [
    path('api/nohbek/', views.login),
    path('api/nohbek/', views.MiModeloList.as_view),
    #path('mi-endpoint/', views.mi_vista)
]
