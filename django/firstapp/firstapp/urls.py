from django.contrib import admin
from django.urls import path
from blog import views

# importe la vue
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home")
# définie la fonction à appeler
]
 