from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from hierarchical_app.models import Tree

admin.site.register(Tree, DraggableMPTTAdmin)