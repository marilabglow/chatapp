from django.contrib import admin
from chatapp.models import Message,UserProfile
class Messageadmin(admin.ModelAdmin):
    list_display = ('id','sender','receiver','message','timestamp','is_read')
admin.site.register(Message,Messageadmin)
class useradmin(admin.ModelAdmin):
    list_display = ('id','user')
admin.site.register(UserProfile,useradmin)
# Register your models here.
