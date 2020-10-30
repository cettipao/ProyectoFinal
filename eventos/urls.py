from django.urls import path
from .views import *

urlpatterns = [
    path('', flyerView),
    path('sms/', smsView),
    path('invitado/<str:num>/<str:conf>/', invitadoView),
    path('invitado/<str:num>/', invitadoView),
    path('administrador/', adminView),
    path('download/', downloadView),
]



