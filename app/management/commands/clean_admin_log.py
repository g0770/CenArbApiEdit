from django.core.management.base import BaseCommand
from django.contrib.admin.models import LogEntry

class Command(BaseCommand):
    help = 'Cleans up the admin log entries'

    def handle(self, *args, **kwargs):
        LogEntry.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleaned admin log entries'))
