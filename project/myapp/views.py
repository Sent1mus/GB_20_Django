from django.shortcuts import render, get_object_or_404
from datetime import datetime as dt, timedelta
from .models import Client, Product, Order

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    context = {
        'title': 'Main page',
    }
    return render(request, 'myapp/index.html', context=context)


def about(request):
    logger.info('About page accessed')
    context = {
        "title": "Обо мне",
        "page_title": "Обо мне",
        "description": "Welcome to our site TODO",
        "github_link": "https://github.com/Sent1mus",
        "my_cave": "My cave"
    }
    return render(request, 'myapp/about.html', context=context)


def products_list(request):
    products = [*enumerate(Product.objects.all().order_by('pk'), start=1)]
    return render(request,
                  'myapp/products_list.html',
                  {'title': 'Product list', 'products': products})


def order_list(request, client_id):
    """
    List of orders for Client with lists of products
    :param request:
    :param client_id: int     -- Client id
    :return:
    """
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client)
    context = {
        'title': 'Order list',
        'client': client,
    }
    if orders:
        context['orders'] = []
        for order in orders:
            context['orders'].append(
                {
                    'order': order,
                    'products': [item for item in order.product.all()],
                }
            )
    return render(request, 'myapp/orders.html', context=context)


def ordered_products_list(request, client_id, period):
    """
    Show products list form orders for defined period
    :param request:
    :param client_id: int
    :param period: str      -- 'week', 'month' or 'year'
    :return:
    """
    client = get_object_or_404(Client, pk=client_id)

    limit = 7 if period == 'week' else 30 if period == 'month' else 365 if period == 'year' else 0

    date_low_lim = (dt.now() - timedelta(limit + 1)).strftime("%Y-%m-%d")
    print(date_low_lim)
    if not limit:
        orders = Order.objects.filter(client=client).order_by('-order_date')
    else:
        orders = Order.objects.filter(client=client).filter(order_date__gt=date_low_lim).order_by('pk')
    context = {
        'title': 'Ordered product list for client',
        'client': client, }
    if orders:
        context['products'] = []
        for order in orders:
            context['products'].extend(
                [
                    {
                        'pk': item.pk,
                        'name': item.name,
                        'price': item.price,
                        'date': order.order_date,
                    }
                    for item in order.product.all()
                ]
            )
    return render(request, 'myapp/ordered_products.html', context=context)


def ordered_products_unique(request, client_id, period):
    """
    Show non-repeated products list form orders for defined period
    :param request:
    :param client_id: int
    :param period: str      -- 'week', 'month' or 'year'
    :return:
    """
    client = get_object_or_404(Client, pk=client_id)

    limit = 7 if period == 'week' else 30 if period == 'month' else 365 if period == 'year' else 0

    date_low_lim = (dt.now() - timedelta(limit + 1)).strftime("%Y-%m-%d")
    print(date_low_lim)
    if not limit:
        orders = Order.objects.filter(client=client).order_by('-order_date')
    else:
        orders = Order.objects.filter(client=client).filter(order_date__gt=date_low_lim).order_by('-order_date')
    context = {
        'title': 'Ordered product list for client (non-repeating)',
        'client': client,
    }
    if orders:
        products_total = set()
        for order in orders:
            products_total.update([*order.product.all()])
        context['products'] = [
            {
                'pk': item.pk,
                'name': item.name,
                'price': item.price,
            }
            for item in sorted(products_total, key=lambda x: x.price)
        ]
    return render(request, 'myapp/ordered_products_unique.html', context=context)
