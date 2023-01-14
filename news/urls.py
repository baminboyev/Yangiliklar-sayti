from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',home, name='home'),
    path('all-news/', AllNews.as_view(), name='all-news'),
    path('category/<int:id>', category, name='category-news'),
    path('region/<int:id>', region, name='region-news'),
    path('detail/<int:id>', detail, name='detail'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
