
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('demopostgre.urls')),
    path('app2/', include('app2.urls')),
    path('app3/', include('app3.urls')),
    path('app4/', include('app4.urls'))

]
