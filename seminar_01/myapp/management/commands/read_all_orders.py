from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Get some fake orders."

    def handle(self, *args, **kwargs):
        result_string = ''
        orders = Order.objects.all()
        if not orders:
            self.stdout.write("No orders found.")
            return

        for order in orders:
            result_string += str(order) + '\n\nProducts:\n'
            result_string += ('~' * 10) + '\n'
            result_string += '\n'.join([str(item) for item in order.product.all()])
            result_string += '\n' + ('=' * 120) + '\n'
        self.stdout.write(result_string)