from rest_framework import serializers
from api.models import *


class RoomSerializers(serializers.ModelSerializer):

	class Meta:
		model = Room
		fields = '__all__'

class ReservationSerializers(serializers.ModelSerializer):
	
	class Meta:
		model = Reservation
		fields = '__all__'