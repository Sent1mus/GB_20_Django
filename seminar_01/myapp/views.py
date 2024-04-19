from django.shortcuts import render

# Create your views here.

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    HTML_block = "<head><title>Главная</title></head>" \
                 "<body>" \
                 "<a href='/'>Главная</a><br>" \
                 "<a href='/about'>Обо мне</a><br>" \
                 "</body>"
    return HttpResponse(HTML_block)


def about(request):
    logger.info('About page accessed')
    HTML_block = "<head><title>Обо мне</title></head>" \
                 "<body>" \
                 "<a href='/'>Главная</a><br>" \
                 "<a href='/'>Обо мне</a><br>" \
                 "<h1>Обо мне</h1><br>" \
                 "<p>I'm Batman</p>" \
                 "<a href='https://github.com/Sent1mus'>My cave</a><br>" \
                 "</body>"
    return HttpResponse(HTML_block)
