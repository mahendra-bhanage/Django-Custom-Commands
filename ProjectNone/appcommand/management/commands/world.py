from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Help message for the user to understand the use of commands.'

    def add_arguments(self, parser):
        parser.add_argument('argss', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            for arg in options['argss']:
                self.stdout.write(self.style.SUCCESS(' %s World!!' % arg))
        except Exception as e:
            raise CommandError(e)