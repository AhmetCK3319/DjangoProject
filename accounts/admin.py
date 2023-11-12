from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,UserProfile
from django.utils.html import format_html

class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','date_joined','last_login','is_active')

    #daha fazla alanın tıklanabilir olması için
    list_display_links=('email','first_name','last_name')

    # üzerinde oynama yapılması istenmeyen alanlar
    readonly_fields=('date_joined','last_login')

    # en son join olanı başta göstermek için
    ordering=('-date_joined',)

    filter_horizontal=()
    list_filter=()
    fieldsets=()


admin.site.register(Account,AccountAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    def thumbnail(self,object):
        return format_html('<img src="{}" width="50" style=" border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description='Profile Picture'

    list_display=('user','city','state','country','thumbnail')
    list_display_links=('thumbnail','user','city','state','country')
