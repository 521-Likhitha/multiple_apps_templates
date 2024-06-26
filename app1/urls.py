from django.urls import path
from app1.views import *
app_name='any'

urlpatterns=[
    path('msg/',msg,name='msg'),
    path('test2/',test2,name='test2'),
]