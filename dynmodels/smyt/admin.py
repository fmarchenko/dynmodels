# -*- coding: utf-8 -*-
from django.contrib import admin
from smyt.models import get_app_models


for model in get_app_models():
    try:
        admin.site.register(model)
    except Exception as ex:
        print ex.message
