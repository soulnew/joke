# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jokebody.models import JokeBody, JokeType
import random
from  django.shortcuts import render_to_response
import sys

reload(sys)                      # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')


def hello(request):
    am = JokeBody.objects.all().count()

    fs = []
    pageItem = 5
    for i in range(0, pageItem):
        id = int(random.random() * am)
        jb = JokeBody.objects.all()[id];
        fs.append(jb)

    return render_to_response("pa/v.html", {'fs': fs})


def search(request):
    fs = []
    pageItem = 5

    if 'keywork' in request.GET and request.GET['keywork']:
        q = request.GET['keywork']
        rs = JokeBody.objects.filter(content__icontains=q)
        # print str(rs.query)
        fs = rs[0:pageItem]
    else:
        am = JokeBody.objects.all().count()

        pageItem = 5
        for i in range(0, pageItem):
            id = int(random.random() * am)
            jb = JokeBody.objects.all()[id];
            fs.append(jb)

    return render_to_response("pa/v.html", {'fs': fs})


def singleSearch(request):
    fs = []

    if 'keywork' in request.GET and request.GET['keywork']:
        q = request.GET['keywork']
        number_of_records = JokeBody.objects.filter(content__icontains=q).count()
        if(number_of_records>0):

            random_index = int(random.random() * number_of_records)
            print ("show id %s" % random_index)
            fs.append(JokeBody.objects.filter(content__icontains=q)[random_index])
    else:
        am = JokeBody.objects.all().count()
        pageItem = 5
        for i in range(0, pageItem):
            id = int(random.random() * am)
            jb = JokeBody.objects.all()[id];
            fs.append(jb)

    return render_to_response("pa/single.html", {'fs': fs})
