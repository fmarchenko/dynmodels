# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse
import re

register = template.Library()

@register.simple_tag(takes_context=True)
def get_verbose_name(context, obj): 
    return obj._meta.verbose_name.title()

@register.simple_tag(takes_context=True)
def get_verbose_name_plural(context, obj): 
    return obj._meta.verbose_name_plural.title()

@register.simple_tag(takes_context=True)
def get_class_name(context, obj): 
    return obj.__class__.__name__

@register.simple_tag
def get_data_url(obj):
    return reverse('get_data', args=[obj.__class__.__name__])

@register.simple_tag
def set_data_url(obj):
    return reverse('set_data', args=[obj.__class__.__name__])

@register.simple_tag
def url_is_active(obj, url):
    return reverse('set_data', args=[obj.__class__.__name__]) == url