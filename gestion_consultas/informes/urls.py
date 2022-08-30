from django.urls import path, include
from . import views

urlpatterns = [
    
   path('informes/', views.informes , name="informes" ),
   path('', views.inicio , name="inicio" ),
   path('about/', views.about , name="about"),
   path('ventas/', views.ventas, name="ventas" ),
   path('pdf/',views.pdf, name="pdf"),
   path('maquinas/',views.maquinas, name="maquinas")
    
]