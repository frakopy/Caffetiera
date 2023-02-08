from django.urls import path
from .views import *

urlpatterns = [
    path('<int:page_id>', sample, name='sample'),
]
