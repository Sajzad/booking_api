from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.db.models import Q

from .models import *
from .serializers import *

# Create your views here.


class RoomListAPIView(APIView):

	def get(self, request, format=None):
		rooms_qs = Room.objects.all()
		try:
			if Room.objects.filter(room_no=room_no).exists():
				res = {
					"msg":"Room already exists",
					"success":False,
					"data":None
				}
				return Response(data=res, status=status.HTTP_400_BAD_REQUEST)
			serializers = RoomSerializers(rooms_qs, many=True)
			res = {
		        "msg": "Room Details",
		        "success": True,
		        "data":serializers.data,}
			return Response(data=res, status=status.HTTP_200_OK)
		except Exception as e:
			res = {
		        "msg": str(e),
		        "success": False,
		        "data":None}
			return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

class CreateRoomAPIView(APIView):

	def post(self, request, format=None):
		try:
			req = request.data
			if not Room.objects.filter(room_no=req.get("room_no")).exists():
				serializer = RoomSerializers(data=req)
				if serializer.is_valid():
					serializer.save()
					res = {
						"msg": "Room added Succesfully",
						"success":True,
						"data": serializer.data
					}
					return Response(data=res, status=status.HTTP_200_OK)

				res = {"msg":str(serializer.errors), "success":False, "data":None}
				return Response(data=res, status=status.HTTP_400_BAD_REQUEST)

			res = {"msg":"Room number already exists!", "success":False, "data":None}
			return Response(data=res, status=status.HTTP_200_OK) 
		except Exception as e:
			res = {"msg":str(e), "success":False, "data":None}
			return Response(data=res, status=status.HTTP_400_BAD_REQUEST)
			
class BookingApiView(APIView):

	def post(self, request, format=None):
		req = request.data
		req['total_price'] = Room.objects.get(id = req.get("room")).price
		serializer = ReservationSerializers(data=req)
		if serializer.is_valid():
			if not serializer.validated_data['check_in'] > serializer.validated_data['check_out']:
				check_out_date = req['check_out'].split("T")[0]
				check_in_date = req['check_in'].split("T")[0]
				reservations = Reservation.objects.filter(
					room_id = req.get('room'),
					check_out__date__gte = check_in_date.strip())
				if not reservations.exists():
					serializer.save()
					res = {
						"msg": "Room is reserved Succesfully!",
						"success":True,
						"data":serializer.data
					}
					return Response(data=res, status=status.HTTP_200_OK)
				res = {"msg":"room is already booked!", "success":True, "data":None}
				return Response(data=res, status=status.HTTP_200_OK)
			else:
				res = {"msg":"Check in should be less than Check out date!", "success":True, "data":None}
				return Response(data=res, status=status.HTTP_200_OK)
		res = {"msg":serializer.errors, "success":False, "data":None}
		return Response(data=res, status=status.HTTP_400_BAD_REQUEST)


class RservationAPIView(APIView):

	def get(self, request, format=None):
		reservation_qs = Reservation.objects.all()
		serializer = ReservationSerializers(reservation_qs, many=True)
		res = {
	        "msg": "Reservation Details",
	        "success": True,
	        "data":serializer.data
	    }
		return Response(data=res, status=status.HTTP_200_OK)