from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now=True)

    def __str__(self):
        return (f'Client:\n{self.name}\n{self.email}\n'
                f'{self.phone}\n{self.address}\n'
                f'{self.registration_date}')


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    add_date = models.DateField(auto_now=True)
    p_image = models.ImageField(upload_to='images/', default=None, null=True)

    def __str__(self):
        return (f'{self.name}:\n'
                f'Price: {self.price}\n'
                f'Amount left: {self.amount}\n'
                f'Description: {self.description}\n'
                f'Added on: {self.add_date}\n')


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    order_date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return (f'Client: {self.client.name} ({self.client.email})\n'
                f'Total price: {self.total_price}\n'
                f'Order date: {self.order_date}\n')
