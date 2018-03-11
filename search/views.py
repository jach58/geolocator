# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.shortcuts import render
from .utils import yelp_search


class SearchView(View):
    def get(self, request, *args, **kwargs):
        items = []
        q = request.GET.get('q')
        loc = request.GET.get('loc')

        if not loc:
            location = request.session.get('CITY', 'Newport Beach')
        else:
            location = loc

        if q:
            items = yelp_search(keyword=q, location=location, request=request)
            return render(request, 'search/home.html', {'results': items})
        return render(request, 'search/home.html', {'results': items})
