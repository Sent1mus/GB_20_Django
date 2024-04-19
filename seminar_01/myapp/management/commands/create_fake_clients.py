from django.core.management.base import BaseCommand
from myapp.models import Client

import random


class Command(BaseCommand):
    help = "Generate some fake customers."

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='Amount of fake users to generate.')

    def handle(self, *args, **kwargs):
        amount = kwargs.get('amount')
        for _ in range(amount):
            Client(
                name=f'name{random.randint(1, 1000)}',
                email=f'mail{random.randint(1, 1000)}@mail.ru',
                phone=f'+7{random.randint(9000000000, 9999999999)}',
                address=f'address{random.randint(1, 1000)}',
            ).save()
        self.stdout.write(f"Added {amount} clients.")