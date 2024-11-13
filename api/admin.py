from django.contrib import admin
from api import models as api_models

admin.site.register(api_models.Service)
admin.site.register(api_models.Project)

