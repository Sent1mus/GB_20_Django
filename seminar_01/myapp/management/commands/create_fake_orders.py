from django.core.management.base import BaseCommand
from random import sample, randint as rin

from myapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Generate fake orders."

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help='Amount of persons ordered something.')
        parser.add_argument('uplimit', type=int, help='Upper limit for amount of orders per person.')

    def handle(self, *args, **kwargs):
        amount = Client.objects.count()
        amount = kwargs.get('amount') if kwargs.get('amount') < amount else amount
        uplimit = Product.objects.count()
        uplimit = kwargs.get('uplimit') if kwargs.get('uplimit') < (uplimit // 10) else 10

        persons = sample(list(Client.objects.all()), amount)
        products = Product.objects.all()
        for pers in persons:
            total_price = 0
            prod_set = sample(list(products), rin(1, uplimit))
            for prod in prod_set:
                total_price += prod.price
            order_tmp = Order(
                client=pers,
                total_price=total_price,
            )
            order_tmp.save()
            for prod in prod_set:
                order_tmp.product.add(prod)
            order_tmp.save()