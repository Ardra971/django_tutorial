from django.contrib import admin
from .models import departments, Doctors,bookings
# Register your models here.
admin.site.register(departments)
admin.site.register(Doctors)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date', 'booked_on')
    list_filter = ('booking_date',)
    search_fields = ('p_name', 'p_email', 'doc_name__doc_name')
    ordering = ('-booking_date',)
admin.site.register(bookings, BookingAdmin)