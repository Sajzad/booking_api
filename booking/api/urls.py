from django.urls import path
from .views import *



app_name = 'api'


urlpatterns = [
    path('rooms/', RoomListAPIView.as_view(), name='rooms'),
    path('create-room/', CreateRoomAPIView.as_view(), name='create-room'),
    path('book-room/', BookingApiView.as_view(), name='booking'),
    path('reservation/', RservationAPIView.as_view(), name='reservation')
]
