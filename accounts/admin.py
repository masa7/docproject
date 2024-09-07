from django.contrib import admin

# Register your models here.
# import CustomUser
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    '''
    class to register column to show record list in admin page
    '''
    # show id and username in record list
    list_display = ('id', 'username')
    # setup link to column
    list_display_links = ('id', 'username')

#register CustomUser.CustomUserAdmin to Django admin site
admin.site.register(CustomUser, CustomUserAdmin)

