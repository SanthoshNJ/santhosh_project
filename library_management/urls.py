from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return HttpResponse("<h1>Welcome to the Library Management System</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/', include('books.urls')),  
    path('', home, name='home'), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]
