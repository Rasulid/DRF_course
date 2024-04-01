from .views import *
from django.urls import path

urlpatterns = [
    path('women-list/', WomenAPIList.as_view(), name='women_list'),
    path('women-update/<int:pk>/', WomenAPIUpdate.as_view(), name='women_update'),
    path('women-destroy/<int:pk>/', WomenAPIDestroy.as_view(), name='women_detail')
]