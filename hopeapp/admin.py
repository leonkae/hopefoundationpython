from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Announcements)
admin.site.register(Events)
admin.site.register(Newsletter)
admin.site.register(Programmes)
admin.site.register(Team)
admin.site.register(Gallery)
admin.site.register(Connect)
# admin.site.register(Donation)
# admin.site.register(Volunteer)
admin.site.register(Mission)
admin.site.register(Vission)
admin.site.register(About)

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "email", "amount")
    search_fields = ("name", "email", "mpesa_code")
    # list_filter = ("created_at")

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    # list_filter = ("created_at")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "email")
    search_fields = ("name", "email", "phone_number")
    # list_filter = ("created_at")
