from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from django.contrib.auth.admin import UserAdmin
from hierarchical_app.models import MyUser, Tree

admin.site.register(MyUser, UserAdmin)
admin.site.register(Tree, DraggableMPTTAdmin)