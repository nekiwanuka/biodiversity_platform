from django.contrib import admin
from .models import * #Tutor, Student, Goo

# Register your models here.
admin.site.register(Contributor)
admin.site.register(Master)
admin.site.register(FgfUser)
admin.site.register(EmailVerificationToken)