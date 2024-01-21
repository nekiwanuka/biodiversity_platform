from django.contrib import admin
from .models import CustomUser, Superuser, Masteruser, Contributor

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'gender', 'profession', 'date_joined')
    search_fields = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

class SuperuserAdmin(admin.ModelAdmin):
    list_display = ('get_email', 'get_phone_number', 'get_gender', 'get_profession', 'get_date_joined')
    search_fields = ('superuser__email',)

    def get_email(self, obj):
        return obj.superuser.email

    def get_phone_number(self, obj):
        return obj.superuser.phone_number

    def get_gender(self, obj):
        return obj.superuser.gender

    def get_profession(self, obj):
        return obj.superuser.profession

    def get_date_joined(self, obj):
        return obj.superuser.date_joined

    get_email.short_description = 'Email'
    get_phone_number.short_description = 'Phone Number'
    get_gender.short_description = 'Gender'
    get_profession.short_description = 'Profession'
    get_date_joined.short_description = 'Date Joined'

admin.site.register(Superuser, SuperuserAdmin)


class MasteruserAdmin(admin.ModelAdmin):
    list_display = ('get_email', 'get_phone_number', 'get_gender', 'get_profession', 'get_date_joined')
    search_fields = ('masteruser__superuser__email',)

    def get_email(self, obj):
        return obj.masteruser.superuser.email

    def get_phone_number(self, obj):
        return obj.masteruser.superuser.phone_number

    def get_gender(self, obj):
        return obj.masteruser.superuser.gender

    def get_profession(self, obj):
        return obj.masteruser.superuser.profession

    def get_date_joined(self, obj):
        return obj.masteruser.superuser.date_joined

    get_email.short_description = 'Email'
    get_phone_number.short_description = 'Phone Number'
    get_gender.short_description = 'Gender'
    get_profession.short_description = 'Profession'
    get_date_joined.short_description = 'Date Joined'

admin.site.register(Masteruser, MasteruserAdmin)

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('get_email', 'get_phone_number', 'get_gender', 'get_profession', 'get_date_joined')
    search_fields = ('contributor__superuser__email',)

    def get_email(self, obj):
        return obj.contributor.superuser.email

    def get_phone_number(self, obj):
        return obj.contributor.superuser.phone_number

    def get_gender(self, obj):
        return obj.contributor.superuser.gender

    def get_profession(self, obj):
        return obj.contributor.superuser.profession

    def get_date_joined(self, obj):
        return obj.contributor.superuser.date_joined

    get_email.short_description = 'Email'
    get_phone_number.short_description = 'Phone Number'
    get_gender.short_description = 'Gender'
    get_profession.short_description = 'Profession'
    get_date_joined.short_description = 'Date Joined'

admin.site.register(Contributor, ContributorAdmin)
