
from django.contrib import admin
from django.urls import path
from  bdeft.views import home,contact,about,products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('products/',products, name='products'),
    path('contact/', contact, name='contact'),
    path('about/',  about, name='about'),
]


