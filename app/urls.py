from django.urls import path
from app.views import *
app_name='any'

urlpatterns=[
    path('hi/',hi,name='hi'),
    path('test1/',test1,name='test1'),
]