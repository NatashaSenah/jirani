from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.jirani,name = 'home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new_neighbourhood/$', views.new_neighbourhood, name='new_neighbourhood'),
    url(r'^business/$', views.business, name='business'),
    url(r'^profile/(\w+)$', views.profile, name='profile'),
    url(r'^accounts/edit/',views.edit_profile, name='edit_profile'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
