from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = "Create groups Editors, Viewers, Admins and assign bookshelf permissions"

    def handle(self, *args, **options):
        Book = apps.get_model('bookshelf', 'Book')

        
        perms_map = {
            'can_view': 'can_view',
            'can_create': 'can_create',
            'can_edit': 'can_edit',
            'can_delete': 'can_delete',
        }

        groups = {
            'Editors': ['can_create', 'can_edit', 'can_view'],
            'Viewers': ['can_view'],
            'Admins': ['can_create', 'can_edit', 'can_view', 'can_delete'],
        }

        for group_name, perm_codenames in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            self.stdout.write(self.style.SUCCESS(f"Group: {group.name} ({'created' if created else 'exists'})"))
            group.permissions.clear()
            for codename in perm_codenames:
                try:
                    perm = Permission.objects.get(content_type__app_label='bookshelf', codename=codename)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Permission {codename} not found for app bookshelf"))
                    continue
                group.permissions.add(perm)
            group.save()

        self.stdout.write(self.style.SUCCESS("Groups and permissions set up successfully."))
