from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('disk/', views.disk,name='desk-use'),
    path('ram/', views.ram,name='ram-use'),
]
