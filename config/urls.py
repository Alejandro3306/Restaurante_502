from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Rutas de tu app
    path('', include('gestion.urls')),

    # ✅ LOGIN
    path('login/', auth_views.LoginView.as_view(template_name='gestion/login.html'), name='login'),

    # ✅ LOGOUT (ESTO SOLUCIONA EL ERROR)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]