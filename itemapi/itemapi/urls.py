from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "Welcome to the Item API"}, status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('items.urls')),  # Include the items API
    path('', home_view),  # Default homepage route
]
