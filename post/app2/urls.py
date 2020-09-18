from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('signup',views.signup, name='signup'),
    path('contact',views.button),
    path('start',views.start, name='on'),
    path('stop', views.stop, name='off'),
    path('details', views.details, name='details'),
    path('contact12', views.contact12, name='contact12'),
]