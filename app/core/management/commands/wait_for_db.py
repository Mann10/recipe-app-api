"""
Django command to wait for the database to be available.
"""
import time
from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for coomand."""
        self.stdout.write('waiting for database....')
        db__up = False
        while db__up is False:
            try:
                self.check(databases=['default'])
                db__up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write(
                    'Database unavailable, waiting 1 second.....')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
