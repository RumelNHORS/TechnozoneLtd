# api/admin.py
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from api import models as api_models

# Custom form for each model to use CKEditor
class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = api_models.Service
        fields = '__all__'
        widgets = {
            'short_description': CKEditorWidget(),
        }

class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = api_models.Project
        fields = '__all__'
        widgets = {
            'short_description': CKEditorWidget(),
        }

class AboutUsAdminForm(forms.ModelForm):
    class Meta:
        model = api_models.AboutUs
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }

# Register the models with custom forms
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

class AboutUsAdmin(admin.ModelAdmin):
    form = AboutUsAdminForm

# Register the models
admin.site.register(api_models.Service, ServiceAdmin)
admin.site.register(api_models.Project, ProjectAdmin)
admin.site.register(api_models.AboutUs, AboutUsAdmin)
