from django.urls import path
from .views import parse_xml

urlpatterns = [
    path('parse/', parse_xml, name='parse_xml'),
]