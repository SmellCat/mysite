# -*- coding:utf-8 -*-

__author = "zhanghaixin"

from django.http import HttpResponse, Http404
import datetime


def hello(request):
    return HttpResponse("Hello world")


def my_homepage_view(request):
    return HttpResponse('a')


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body><html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    # try:
    #     print (offset)
    #     offset = int(offset)
    # except ValueError:
    #     raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hours(s）, it will be %s." \
           "</body></html>" % (offset, dt)
    return HttpResponse(html)

