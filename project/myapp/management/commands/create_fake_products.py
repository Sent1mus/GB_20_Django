from django.core.management.base import BaseCommand
from myapp.models import Product
import random


class Command(BaseCommand):
    help = "Generate fake products."

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='Amount of fake users to generate.')

    def handle(self, *args, **kwargs):
        amount = kwargs.get('amount')
        for _ in range(amount):
            Product(
                name=f'product{random.randint(1, 10000)}',
                description=f'any description{random.randint(1, 10000)}',
                price=random.uniform(99, 99999),
                amount=random.randint(0, 50),
            ).save()
        self.stdout.write(f"Added {amount} products.")