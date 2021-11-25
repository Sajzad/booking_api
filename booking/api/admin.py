from django.contrib import admin

from .models import *

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'room_no',
        'price',
    )

class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'room',
        'total_price',
    	'created_at',
    	'check_in',
        'check_out',
    )

admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
