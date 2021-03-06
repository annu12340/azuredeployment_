
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('', include('post.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('authenticate.urls')),
    path('post/', include('post.urls')),
     path('pay/', include('payment.urls')),
]
