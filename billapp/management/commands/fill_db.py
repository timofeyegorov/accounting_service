from django.core.management.base import BaseCommand
from billapp.models import PeopleName, OperationType, OperationTag, Operation

class Command(BaseCommand):

    def handle(self, *args, **options):
        Operation.objects.create(
            operation_sum = 10000,
            people_name = Operation.objects.get(people_name_id=1)
        )

        print('End')