from django.urls import path

from WebScraper.common.views import index

urlpatterns = [
    path('', index, name='index')

]