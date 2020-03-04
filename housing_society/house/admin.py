from django.contrib import admin
from house.models import Member, Notice

# Register your models here.

admin.site.site_header = 'Housing Society Admin Dashboard'
admin.site.site_title = 'Admin Page'
admin.site.register(Member)
admin.site.register(Notice)
