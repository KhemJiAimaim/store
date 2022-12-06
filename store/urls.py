from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('' , views.index, name='index'),
    path('add/' , views.product_add, name='product_add'),
    path('delete/<int:id>' , views.delete, name='delete'),

    

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)