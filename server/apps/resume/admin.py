from django.contrib import admin

from .models import ContactInfo, Character, Skill, Education, Certificate, Job, Project, SocialNetwork


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone', 'email')
    list_display_links = ('name',)

    def has_add_permission(self, request):
        """Функция не дает добавлять объектов больше, чем 'max_objects' """
        max_objects = 1
        if self.model.objects.count() >= max_objects:
            return False
        return super().has_add_permission(request)


@admin.register(Character)
class MyHobbyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


@admin.register(Skill)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')
    list_display_links = ('name',)
    list_editable = ('score',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_for', 'date_to')
    list_display_links = ('name',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'score', 'date')
    list_display_links = ('name',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('organisation', 'position', 'date_for', 'date_to')
    list_display_links = ('organisation',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


@admin.register(SocialNetwork)
class SocialNetwork(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


admin.site.site_title = 'My resume v2'
admin.site.site_header = 'My resume v2'
