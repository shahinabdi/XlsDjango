from django.urls import path
from . import views
from renoir_xlsdb import settings
from django.conf.urls.static import static
urlpatterns =[
path("",views.upload_file,name="upload_file")
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)