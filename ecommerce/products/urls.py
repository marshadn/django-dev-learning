from django.urls import path
from .views import index,details,create,delete,update

app_name='products'


urlpatterns = [
    path('',index),
    path('<int:id>/',details),
    path('<int:id>/delete/',delete),
    path('<int:id>/update/',update),
    path('create/',create)
]
