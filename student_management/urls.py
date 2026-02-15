from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

def home(request):
    return redirect('student_home')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path(
    'logout/',
    auth_views.LogoutView.as_view(),
    name='logout'
    ),
    path('students/', include('students.urls')),
]
