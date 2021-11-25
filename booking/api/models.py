from django.db import models

# Create your models here.

class Room(models.Model):
	room_no = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=5000, decimal_places=4)

	def __str__(self):
		return str(self.room_no)

class Reservation(models.Model):
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	total_price = models.DecimalField(max_digits=20000, decimal_places=4)
	check_in = models.DateTimeField()
	check_out = models.DateTimeField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.room.room_no)
