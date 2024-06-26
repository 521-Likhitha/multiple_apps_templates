from django.urls import path
from app2.views import *
app_name='any'

urlpatterns=[
    path('bye/',bye,name='bye'),
    path('test3/',test3,name='test3')
]