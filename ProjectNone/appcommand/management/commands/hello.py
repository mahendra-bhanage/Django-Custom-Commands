from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Help message for the user to understand the use of commands.'

    def add_arguments(self, parser):
        parser.add_argument('user_name', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            for user in options['user_name']:
                self.stdout.write(self.style.SUCCESS('Hello "%s"' % user))
        except Exception as e:
            raise CommandError(e)