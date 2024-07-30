from django.contrib import admin
from django.urls import path
from .views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home")
    #Al poner "" sin nada en su interior, indica que la página principal presentará la vista HomeView 
    #Utilizamos el .as_view() porque estamos trabajando con una clase, de no utilizarla el programa no funcionaría correctamente:
    #Colocamos el name para hacer referencia a la clase
]
